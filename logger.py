#!/usr/bin/env python
"""
logger.py - Phenny Room Logging Module
Author: Peter Higgins (dante@dojotoolkit.org)
About: http://higginsforpresident.net
License: AFL | New BSD
"""

import os, time;

def get_file(phenny, chan):
    return phenny.nick + "-" + phenny.config.host + "-" + chan + ".log.db"

def setup(self): 

    # if we don't explicitly list channels to log, log them all:
    if not hasattr(self.config, "logchannels"):
        self.config.logchannels = self.config.channels

    # make the logdir path if not there
    self.logdir = os.path.join(os.path.expanduser('~/.phenny/'), 'logs');
    if not os.path.exists(self.logdir):
        os.mkdir(self.logdir);

    # create a series of files as stubs
    for channel in self.config.logchannels:
        log_filename = os.path.join(self.logdir, get_file(self, channel))
        if not os.path.exists(log_filename): 
            try: f = open(log_filename, 'w')
            except OSError: pass
            else: 
                f.write('')
                f.close()
               

def log_message(phenny, teller, chan, msg):
    # only log the channels we care about
    if chan in phenny.config.logchannels:
        timenow = time.time()
        line = "\t".join((str(timenow), chan, teller, msg))
        try: f = open(os.path.join(phenny.logdir, get_file(phenny, chan)), "a")
        except OSError: pass
        else:
            f.write(line + "\n")
            f.close();
            
def loggit(phenny, input):
    msg = input.group(1).encode('utf-8')
    log_message(phenny, input.nick, input.sender, msg)
loggit.rule = r'(.*)'
loggit.priority = 'high'    

if __name__ == '__main__': 
   print __doc__.strip()
