#!/usr/bin/env python

import os
import sys
import signal
import eZ430
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=DeprecationWarning)
    
    import xmpp
    
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


# Google talk connection with Jabber/XMPP
username = ""  # @gmail.com 
password = ""
listOfRecipients = ['user@gmail.com'] 
message1 = "Hi
message2 = "Hello world!!"
message3 = "From Chronos with love"

jid = xmpp.protocol.JID(username)
xmppClient = xmpp.Client(jid.getDomain(), debug=[])
xmppClient.connect(server=('talk.google.com', 5223))
xmppClient.auth(jid.getNode(), password)
xmppClient.sendInitPresence()

while 1:
    data = chronos.read()
    button = int(ord(data[6]))
    
    if(button == 18):
        if(verbose): print "Right pressed."
        for recipient in listOfRecipients:
            xmppClient.send(xmpp.Message(recipient, message1))
        chronos.debounce()
        
    elif(button == 50):
        if verbose: print "Left pressed."
        for recipient in listOfRecipients:
            xmppClient.send(xmpp.Message(recipient, message2))
        chronos.debounce()
        
    elif(button == 34):
        if verbose: print "Home pressed."
        for recipient in listOfRecipients:
            xmppClient.send(xmpp.Message(recipient, message3))
        chronos.debounce()
