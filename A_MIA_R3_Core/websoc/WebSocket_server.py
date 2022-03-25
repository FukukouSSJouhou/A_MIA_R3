import logging

from websocket_server import WebsocketServer
class WebSocket_server():
    def __init__(self,host,port=5001):
        self.server=WebsocketServer(port,host=host,loglevel=logging.INFO)

    def new_client(self, client, server):
        print("new client connected and was given id {}".format(client['id']))
    def client_left(self, client, server):
        print("client({}) disconnected".format(client['id']))

    def message_received(self, client, server, message):
        pass
