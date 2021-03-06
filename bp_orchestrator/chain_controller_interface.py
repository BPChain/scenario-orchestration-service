"""I offer the interface for the the chain controller to send me data"""

# pylint: disable = too-few-public-methods, invalid-name, broad-except

import json
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from .meta_scenario import SETTINGS_SYNC
from .project_logger import set_up_logging

LOG = set_up_logging(__name__)


class ControllerInterface(WebSocket):

    def handleMessage(self):
        print(self.data)
        try:
            json_data = json.loads(self.data)
            SETTINGS_SYNC.put(json_data)
        except Exception as error:
            LOG.error('Error when handling incoming message from controller: %s', error)


def start_controller_server(port: int):
    server = SimpleWebSocketServer('', port, ControllerInterface)
    server.serveforever()
