from typing import Dict


class AbstractSetup:

    def __init__(self):
        pass

    def prepare(self, slave):
        pass


class AbstractSlave:
    def __init__(self, config: Dict, setup: AbstractSetup):
        pass

    def is_alive(self) -> bool:
        pass

    def transact(self, name: str, hex_string: str):
        pass
