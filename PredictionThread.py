#!/usr/bin/python
import threading
from threading import Thread
import socket
from PredictionProcess import PredictionProcess
from time import time


class Prediction(Thread):

    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.conn.settimeout(30.0)
        self.addr = addr
        self.stop = False

    def run(self):
        try:
            startTime = time()
            features = self.conn.recv(1024)
            self.conn.send(str(self.call_prediction_method(features)))
            # self.conn.sendall(repr(features))
            print "Time Spent Total:", (time() - startTime), "us"
            self.stop_thread()
        except:
            print "Connection Error"
            self.stop_thread()

    def call_prediction_method(self, features):
        try:
            prediction = PredictionProcess(features, algorithm="DT")
            rst = prediction.prediction()
        except:
            print "Not running algorithms"
            self.stop_thread()
        return rst

    def stop_thread(self):
        self.stop = True
        self.conn.close()