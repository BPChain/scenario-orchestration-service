from setuptools import setup

setup(name='bp_orchestrator',
      version='0.5',
      description='Orchestrate blockchain scenarios',
      author='Anton von Weltzien',
      license='MIT',
      packages=['bp_orchestrator'],
      url='https://github.com/BPChain/scenario-orchestration-service.git',
      install_requires=[
          'SimpleWebSocketServerFork==0.1.3',
      ],
      zip_safe=False)
