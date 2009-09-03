#!/usr/bin/env python
"""
trac.py - Phenny Dojo/Trac Module
Author: Peter Higgins (dante@dojotoolkit.org)
About: http://higginsforpresident.net
"""

import web

def ticket(phenny, input):
    url = 'http://bugs.dojotoolkit.org/ticket/'
    id = input.group(1);
    response = web.get(url + id + '?format=tab');
    lines = response.split("\n", 1); #drop first line
    out = ""
    try:
        # ugh, need to switch to CVS. This breaks if description has tab-spaced code inside.
        tid, summary, reporter, owner, description, type, status, priority, milestone, component, version, severity, resolution, keywords, cc = lines[1].split("\t")
    except ValueError: 
        phenny.say(lines[1]);
        out = "I couldn't find a ticket with that id."
        pass
    else:
        out = input.nick + ": " + summary + " [" + status + "/" + resolution + "] see: " + url + id;
        
    phenny.say(out);
ticket.rule = r'(?i)#([0-9]+)\b'

def apicheck(phenny, input):
    namespace, api = input.groups()
    # phenny.say(namespace + "." + api)
apicheck.rule = r'(?i)\?(dojox?|dijit)\.(.*)\??'

# we can open a java/rhino proc, and pipe stuff there, no? v8?
#def execjs(phenny, input):
#    phenny.say("running" + input.group(1))
#execjs.rule = r'^\.eval\ (.*)$'

if __name__ == '__main__': 
   print __doc__.strip()
