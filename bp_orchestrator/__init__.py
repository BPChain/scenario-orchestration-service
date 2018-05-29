"""I provide the function orchestrate to be used on a master node in a blockchain to controll
the scenario execution on the slave nodes (other nodes) in that network"""

# lets python know this is a module
from .abstract import AbstractSetup, AbstractSlave
from .run_threads import orchestrate
