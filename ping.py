#!/usr/bin/env python
"""
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com (with small modifications from Peter Higgins [dante@dojotoolkit.org])
About: http://inamidst.com/phenny/
"""

import random

def hello(phenny, input): 
   greeting = random.choice(('Hi', 'Hey', 'Hello', input.group(1)))
   punctuation = random.choice(('', '!', '...', '. hoe gaat het?'))
   phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|h[ie]ya?|moin|morning) $nickname\b'

def thanks(phenny, input):
    salutation = random.choice(('np', 'yw', 'anytime', 'de nada.'))
    phenny.say(input.nick + ': ' + salutation);
thanks.rule = r'(?i)(thanks|thank\ you|danke) $nickname\b'
    
def interjection(phenny, input): 
   phenny.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'
interjection.thread = False

if __name__ == '__main__': 
   print __doc__.strip()
