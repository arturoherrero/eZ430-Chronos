#!/usr/bin/env python

import os, eZ430

YES = 1
NO = 0

verbose = YES
chronos = eZ430.Chronos()

if verbose:
    print "Opening eZ430 on", chronos.dev

if (os.system("xdotool --version") != 0):
    print "You need xdotool."
    os.exit(1)
    
while 1:
    data = chronos.read(7)
    x = ord(data[0])
    y = ord(data[1])
    z = ord(data[2])
    
    if verbose:
		if x != 0 and y != 0 and z != 0:
			print "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
