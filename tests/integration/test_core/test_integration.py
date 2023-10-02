import asyncio
import time
from pathlib import Path
from unittest import TestCase

from pycdp.core.chrome import Chrome
from pycdp import Chrome


class Tests(TestCase):
    def test_open_tab(self):
        async def _():
            chrome = Chrome.create().start()

            time.sleep(1)
            path = Path('tests/integration/test.html').absolute().as_uri()

            chrome.open_tab(tab_url=path)

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.start_session()

            print(await target.send_and_await_response(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            ))

        asyncio.get_event_loop().run_until_complete(_())

    def test(self):
        async def _():
            chrome = Chrome.create().start()

            time.sleep(1)

            targets = chrome.get_targets()
            target = targets[0]

            await target.connect()
            await target.start_session()

            print(await target.send_and_await_response(
                'Page.enable'
            ))

            print(await target.send_and_await_response(
                'Network.enable'
            ))

            await target.send(
                'Debugger.enable',
            )

            reader = target.open_stream(['Page.frameStoppedLoading'])

            await target.send_and_await_response(
                'Page.navigate',
                {
                    'url': 'https://google.com'
                }
            )

            async for event in reader.iterate():
                print(event)
                break

            result = await target.send_and_await_response(
                'Runtime.evaluate',
                {
                    'expression': 'document.querySelector("form")'
                }
            )

            print(result)

        asyncio.get_event_loop().run_until_complete(_())