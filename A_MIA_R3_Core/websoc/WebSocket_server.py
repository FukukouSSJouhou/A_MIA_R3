import asyncio
import json
import logging

from websocket_server import WebsocketServer

from A_MIA_R3_Core.websoc.WebSocImgSelectCallback import WebSocImgSelectCallback


class WebSocket_server():
    def __init__(self,host,callback:WebSocImgSelectCallback,port=5001):
        self.server=WebsocketServer(port,host=host,loglevel=logging.INFO)
        self.callback:WebSocImgSelectCallback=callback

    def new_client(self, client, server):
        print("new client connected and was given id {}".format(client['id']))
    def client_left(self, client, server):
        print("client({}) disconnected".format(client['id']))

    def message_received(self, client, server, message):
        jd=json.loads(message)
        commandkun=jd['command']
        if(commandkun=="selectedimg"):
            dataindex=jd['indexid']
            self.callback.execute(dataindex)
    def run(self):
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_in_executor(self.server)
