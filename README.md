# scenario-orchestration-service
[![Maintainability](https://api.codeclimate.com/v1/badges/05758af556fd6ab9d0c1/maintainability)](https://codeclimate.com/github/BPChain/scenario-orchestration-service/maintainability)

[![Build Status](https://travis-ci.org/BPChain/scenario-orchestration-service.svg?branch=master)](https://travis-ci.org/BPChain/scenario-orchestration-service)

Orchestrate a Scenario provided by the middleware. This will be done by the 'master' node of a blockchain.

To install run: ```pip install git+https://github.com/BPChain/scenario-orchestration-service.git```
<br/> Do this before running ```pip install -r requirements.txt```
<br /> import and use `orchestrate(port: int, slave_class: Type[AbstractSlave], 
setup=AbstractSetup()):` to run the service. You need to pass a Slave class which encapsulates 
the communication with the slaves. You can pass a setup object that sets up things on the 
blockchain or prepares slaves if necessary.  
