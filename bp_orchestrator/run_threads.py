"""I start all the threads necessary to control the slave nodes and receive info from the backend
controller"""
from threading import Thread
from typing import Type

from .abstract import AbstractSetup, AbstractSlave
from .project_logger import set_up_logging
from .chain_controller_interface import start_controller_server
from .http_server import start_slave_server
from .meta_scenario import run_scenario

LOG = set_up_logging(__name__)


def orchestrate(port: int, slave_class: Type[AbstractSlave], setup=AbstractSetup()):
    """I run the orchestration of a scenario. Provide me with I port where I listen to the backend
    Controller. I also need a Slave class that defines how to talk to the slaves. Additionally a
    Setup object can be provided"""
    Thread(target=start_controller_server, args=[port]).start()
    Thread(target=start_slave_server, args=[setup, slave_class]).start()
    Thread(target=run_scenario, args=[]).start()
    LOG.info('All threads started')
