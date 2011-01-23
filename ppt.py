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
    button = int(ord(data[6]))
    
    if(button == 18):
        if(verbose): print "Right pressed."
        #os.system("xdotool click 3")
        chronos.debounce()
        
    elif(button == 50):
        if verbose: print "Left pressed."
        #os.system("xdotool click 1")
        chronos.debounce()
        
    elif(button == 34):
        if verbose: print "Home pressed."
        #os.system("xdotool key Home")
        chronos.debounce()
