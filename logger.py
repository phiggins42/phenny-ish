#!/usr/bin/env python
"""
logger.py - Phenny Room Logging Module
Author: Peter Higgins (dante@dojotoolkit.org)
About: http://higginsforpresident.net
License: AFL | New BSD
"""

import os, time;

def setup(self): 
   # FIXME: a file per room would be better, no?
   fn = self.nick + '-' + self.config.host + '.log.db'
   self.log_filename = os.path.join(os.path.expanduser('~/.phenny'), fn)
   if not os.path.exists(self.log_filename): 
      try: f = open(self.log_filename, 'w')
      except OSError: pass
      else: 
         f.write('')
         f.close()

def log_message(phenny, teller, chan, msg):
    timenow = time.time()
    line = "\t".join((str(timenow), chan, teller, msg))    
    try: f = open(phenny.log_filename, "a")
    except OSError: pass
    else:
        f.write(line + "\n")
        f.close();
            
def loggit(phenny, input):
    teller = input.nick
    chan = input.sender
    msg = input.group(1).encode('utf-8')
    log_message(phenny, teller, chan, msg)
loggit.rule = r'(.*)'
loggit.priority = 'high'    

if __name__ == '__main__': 
   print __doc__.strip()
