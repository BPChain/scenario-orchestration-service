[![Maintainability](https://api.codeclimate.com/v1/badges/05758af556fd6ab9d0c1/maintainability)](https://codeclimate.com/github/BPChain/scenario-orchestration-service/maintainability)
[![Build Status](https://travis-ci.org/BPChain/scenario-orchestration-service.svg?branch=master)](https://travis-ci.org/BPChain/scenario-orchestration-service)

## Scenario Orchestration Service
The this service orchestrates a scenario execution in a blockchain network. It provides a 
framework for the different blockchains where they can supply different implementations for a 
proxy to their slaves.


#### Usage 
Import and use `orchestrate(port: int, slave_class: Type[AbstractSlave], 
setup=AbstractSetup()):` to run the service. You need to pass a Slave class which 
encapsulates 
the communication with the slaves. You can pass a setup class that sets up things on the 
blockchain or prepares slaves if necessary. Slave nodes can send an arbitrary json formatted 
dictionary via http to the master-node at ```Port 60.000```
This service only needs to run on the master node. 

#### Architecture 
The orchestrator is comprised of five major files. [```run_threads```](bp_orchestrator/run_threads.py)
contains the ``orchestrate`` function  which starts the service. 
[`meta_scenario`](bp_orchestrator/meta_scenario.py)
contains the logic to run the scenario. [`http_server`](bp_orchestrator/http_server.py)  accepts 
the connection details from the slaves, creates a new [`Slave`](bp_orchestrator/abstract.py) 
object, and passes it to the orchestration thread via a Queue. The 
[`ControllerInterface`](bp_orchestrator/chain_controller_interface.py) provides an Interface for 
the [`private-chain-controller`](https://github.com/BPChain/private-chain-controller.git) where 
the controller can pass new scenario settings to the orchestrator. It also syncs these settings 
to the orchestration thread via a Queue. 

#### Install 
To install run: ```pip install git+https://github.com/BPChain/scenario-orchestration-service.git```

