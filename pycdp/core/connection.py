import asyncio
import json
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import websockets.client as websockets

from pycdp.core.stream import EventStreamReader, EventStream
from pycdp import logging

_id = 0


def next_rpc_id():
    global _id
    _id += 1
    return _id


def validate_rpc_response(response: dict):
    if 'error' in response and response['error']:
        error = response['error']
        raise Exception(
            'Received the following error: '
            f'Err Code: {error["code"]}, '
            f'Err Message: {error["message"]}, '
            f'Raw Message: {response}'
        )


@dataclass
class Connection:
    stream_readers: defaultdict[str, list[EventStream]] = field(
        init=False,
        repr=False
    )
    in_flight_futures: dict[int, asyncio.Future] = field(
        init=False,
        repr=False
    )
    ws: Optional[websockets.WebSocketClientProtocol] = field(
        init=False,
        repr=False
    )
    ws_listener: Optional[asyncio.Task] = field(
        init=False,
        repr=False
    )
    ws_connected: Optional[asyncio.Future] = field(
        init=False,
        repr=False
    )

    ws_url: str

    @property
    def is_connected(self):
        return self.ws is not None

    def __post_init__(self):
        self.stream_readers = defaultdict(list)
        self.in_flight_futures = {}
        self.ws = None
        self.ws_connected = None
        self.ws_listener = None

    def _handle_event(self, event: dict):
        if logging.is_logging_enabled('connection.handle_event'):
            print(event)

        for stream in self.stream_readers[event['method']]:
            stream.write(event)

    async def _handle_message(self, message: str):
        if logging.is_logging_enabled('connection.handle_message'):
            print(message)

        message = json.loads(message)

        if 'id' in message:
            return self._handle_response(
                message
            )

        else:
            return self._handle_event(
                message
            )

    def _handle_response(self, response: dict):
        if logging.is_logging_enabled('connection.handle_response'):
            print(response)

        future = self.in_flight_futures.pop(
            response['id'],
            None
        )

        if future is None:
            return

        try:
            validate_rpc_response(
                response
            )

            future.set_result(
                response['result']
            )

        except Exception as e:
            future.set_exception(e)

    async def _listen_async(self):
        async with websockets.connect(self.ws_url) as ws:
            self.ws = ws
            self.ws_connected.set_result(
                True
            )

            while True:
                message = await ws.recv()
                await self._handle_message(
                    message
                )

    def close_stream(
            self,
            reader: EventStreamReader
    ):
        for event in reader.events:
            self.stream_readers[event].remove(
                reader.stream
            )

    async def connect(self):
        loop = asyncio.get_event_loop()

        self.ws_connected = loop.create_future()
        self.ws_listener = loop.create_task(self._listen_async())

        await self.ws_connected

    def open_stream(
            self,
            events: list[str]
    ) -> EventStreamReader:
        stream = EventStream.create(
            self,
            events
        )

        for event in events:
            self.stream_readers[event].append(
                stream
            )

        return stream.create_reader()

    async def send(
            self,
            method: str,
            params: dict
    ):
        loop = asyncio.get_event_loop()

        request_id = next_rpc_id()
        request = {
            'id': request_id,
            'method': method,
            'params': params
        }

        request = json.dumps(request)
        future = loop.create_future()

        self.in_flight_futures[request_id] = future

        try:
            await self.ws.send(request)

        except Exception as e:
            future.set_exception(e)

        return future