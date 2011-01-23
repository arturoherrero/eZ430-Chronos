#!/usr/bin/env python

import os
import sys
import signal
import eZ430
import dbus
import time

YES = 1
NO = 0

verbose = NO
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


# Rhythmbox dbus
session_bus = dbus.SessionBus()
proxy_object = session_bus.get_object("org.gnome.Rhythmbox", "/org/gnome/Rhythmbox/Player")
player = dbus.Interface(proxy_object, "org.gnome.Rhythmbox.Player")

# Gestures
def sound():
    print "Gesture detected"
    player.playPause(1)

position = 0
while 1:
    data = chronos.read()
    acc = {'x': ord(data[0]), 'y': ord(data[1]), 'z': ord(data[2])}
    if acc['x'] != 0 and acc['y'] != 0 and acc['z'] != 0:
        x = acc['x']
        y = acc['y']
        z = acc['z']
    
    if verbose:
        print "x: " + str(x) + " y: " + str(y) + " z: " + str(z)

    if (x > 5) and (x < 25) and (y > 200) and (z > 200):    # Hand up
        position += 1
        if position > 150:
            sound()
            position = 0

#player.playPause(1)             # Play/Pause
#player.setVolumeRelative(0.2)   # Volume +20%
#player.setVolumeRelative(-0.2)  # Volume -20%
