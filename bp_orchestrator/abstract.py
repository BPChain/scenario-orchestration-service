"""I hold stubs for the Setup and the Slave classes. To use the orchestration implement the Slave
class to provide communication with the slaves. If necessary implement Setup for setup of the
blockchain at the start"""

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
