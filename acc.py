#!/usr/bin/env python

import os
import sys
import signal
import eZ430

YES = 1
NO = 0

verbose = YES
chronos = eZ430.Chronos()

if verbose:
    print "Opening eZ430 on", chronos.dev

if (os.system("xdotool --version") != 0):
    print "You need xdotool."
    sys.exit(1)
    
def signal_handler(signal, frame):
    print "\nExit program"
    chronos.stop()
    sys.exit(2)
    
signal.signal(signal.SIGINT, signal_handler)


while 1:
    data = chronos.read()
    acc = {'x': ord(data[0]), 'y': ord(data[1]), 'z': ord(data[2])}
    if acc['x'] != 0 and acc['y'] != 0 and acc['z'] != 0:
        x = acc['x']
        y = acc['y']
        z = acc['z']
    
    if verbose:
        print "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
