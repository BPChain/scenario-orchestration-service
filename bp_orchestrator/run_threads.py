"""I start all the threads necessary to control the slave nodes and receive info from the backend
controller"""
from threading import Thread

from .abstract import AbstractSetup, AbstractSlave
from .project_logger import set_up_logging
from .chain_controller_interface import start_controller_server
from .http_server import start_slave_server
from .meta_scenario import run_scenario

LOG = set_up_logging(__name__)


def orchestrate(setup: AbstractSetup, port: int, slave_class=AbstractSlave):
    Thread(target=start_controller_server, args=[port]).start()
    Thread(target=start_slave_server, args=[setup, slave_class]).start()
    Thread(target=run_scenario, args=[]).start()
    LOG.info('All threads started')

