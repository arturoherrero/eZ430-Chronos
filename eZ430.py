#!/usr/bin/env python

import serial

class Chronos():
    
    def __init__(self, dev = "/dev/ttyACM0", deb = 50):
        self.dev = dev
        self.deb = deb
        self.start()
        
    def start(self):
        self.connection = serial.Serial(self.dev, 115200, timeout = 1)
        self.write("\xFF\x07\x03")
        
    def stop(self):
        self.write("\xFF\x07\x03")
        self.connection.close()
        
    def read(self, length = 7):
        self.connection.write("\xFF\x08\x07\x00\x00\x00\x00")
        return self.connection.read(length)
        
    def write(self, message):
        self.connection.write(message)
        
    def debounce(self):
        i = self.deb
        while i:
            self.read()
            i -= 1
