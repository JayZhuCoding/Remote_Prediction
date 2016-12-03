#!/usr/bin/python
import socket
import threading
from threading import Thread
from PredictionThread import Prediction

def _prediction_server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('', 9090))
    connections = []

    while True:
        #accept connections from the outside
        serversocket.listen(1)
        (conn, addr) = serversocket.accept()
        print "Connected by:", addr
        try:
            # get features and do prediction
            t = Prediction(conn, addr)
            t.daemon = True
            connections.append(t)
            t.start()
        except KeyboardInterrupt:
            print "Server Stoped by Keyboard Interruption"
            t.stop_thread()
            t.stop()


if __name__=="__main__":
    _prediction_server()