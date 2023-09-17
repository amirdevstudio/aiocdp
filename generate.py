import logging
import shutil
from pathlib import Path

from generator import ast
from generator.parser import parser
from generator.utils import snake_case
from generator.visitor import SourceCodeGenerator

logging.basicConfig(
    level=logging.DEBUG,
    format='\n%(message)s\n'
)


GENERATED_MODULE_HEADER = '''\
# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

'''


def main():
    protocols = parser.parse([
        'static/protocols/1.3/browser_protocol.json',
        'static/protocols/1.3/js_protocol.json'
    ])

    Path('cdp/domains').mkdir(parents=True, exist_ok=True)
    Path('cdp/domains/__init__.py').touch()

    for item in Path('cdp/domains').iterdir():
        if item.name not in ('__init__.py', 'base.py', 'utils.py'):
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    elapsed = 0

    for protocol in protocols:
        for domain in protocol.domains:
            module_name = snake_case(domain.domain)

            Path(f'cdp/domains/{module_name}').mkdir(parents=True, exist_ok=True)
            Path(f'cdp/domains/{module_name}/__init__.py').touch()

            module = ast.domain.generate(domain)
            module = SourceCodeGenerator().generate(module)
            elapsed += module.generation_time

            Path(f'cdp/domains/{module_name}/domain.py').write_text(
                GENERATED_MODULE_HEADER +
                module.source
            )

            module = ast.modules.types.generate(domain)
            module = SourceCodeGenerator().generate(module)
            elapsed += module.generation_time

            Path(f'cdp/domains/{module_name}/types.py').write_text(
                GENERATED_MODULE_HEADER +
                module.source
            )

    print(
        f'Generated "cdp/domains/*" in '
        f'{elapsed} seconds'
    )

    module = ast.domains.generate(protocols)
    module = SourceCodeGenerator().generate(module)
    print(
        f'Generated "cdp/domains/domains.py" in '
        f'{module.generation_time} seconds'
    )

    Path(f'cdp/domains/domains.py').write_text(
        GENERATED_MODULE_HEADER +
        module.source
    )

    module = ast.mapper.generate(protocols)
    module = SourceCodeGenerator().generate(module)
    print(
        f'Generated "cdp/domains/mapper.py" in '
        f'{module.generation_time} seconds'
    )

    Path(f'cdp/domains/mapper.py').write_text(
        GENERATED_MODULE_HEADER +
        module.source
    )


if __name__ == '__main__':
    main()
