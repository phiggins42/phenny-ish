#!/usr/bin/env python
"""
dojodocs.py - Phenny Dojo API Doc Module
Author: Peter Higgins (dante@dojotoolkit.org)
About: http://higginsforpresident.net
"""

import xml.etree.ElementTree as ET, re, string

lookupCache = {}

def create_sig(el):
    sig = "";
    fn = el.attrib.get("location")
    sig += fn + "(";
    params = el.findall(".//parameter")
    for param in params:
        sig += param.attrib.get("name")
        sig += ", ";
    sig += ")";
    return sig;

def make_link(name):
    bit = string.join(name.split("."),"/")
    return "http://docs.dojocampus.org/" + bit

def load_doc(name):
    return ET.parse(name)

def get_description(el):
    return el.findtext(".//description")

def find_methods(el):
    return el.findall(".//method")

def popit(term):
    
    m = term.split(".");
    last = m.pop();
    newterm = ""
    for base in m:
        newterm += base 
  
    return newterm, last

def run_search(term, detail, command):
    
    if(term in lookupCache):
        item = lookupCache[term]
        out = term + "." + detail + ": "
        methods = find_methods(item);
        shown = False
        link = ""
        for method in methods:
            if(method.attrib.get("name") == detail):
                out += get_description(method)
                link = make_link(term + "." + detail)
                shown = True

        if not shown:
            if (detail == ""):
                link = make_link(term);
                out =  term + " "
                if(command == ""):
                    out += get_description(item)
                if(command == "methods"):
                    out += "methods: "
                    for method in methods:
                        found = method.attrib.get("name")
                        if found:
                            out += found + " "
                            
            else:
                out += get_description(item)
                
        out += " " + link;

        return out
        
    else:
        newterm, last = popit(term);
        if (last == detail): 
            return "buggar?"
            
        return run_search(newterm, last, command)

def do_search(phenny, termy):
    term = termy.group(1)
    m = re.match("(\w+)\.", term);
    command = ""
    if m is not None:
        namespace = m.group(1)
        if not namespace in lookupCache:
            return
    
    parts = term.split(" ")
    if (len(parts) > 1):
        print parts;
        command = parts.pop()
        term = parts[0];
        
    response = run_search(term, "", command)
    if( response != "" ):
        phenny.say(response.replace("\t", "").replace("\n", " "))
        
do_search.rule = r'^(.*)\?$'
        
def run_prompt():
    while True:
        search = raw_input('> ')
        if(search == "."): 
            break
        else: 
            result = do_search(Null, search);
            if( result != "" ):
                print result

def setup(phenny):
    api = load_doc("../api.xml");
    # generate a dictionary of names->Element (so we can query for a <method> in the ns)
    nss = api.findall(".//object");
    for ns in nss:
        name = ns.attrib.get("location");
        lookupCache[name] = ns;

# we can open a java/rhino proc, and pipe stuff there, no? v8?
#def execjs(phenny, input):
#    phenny.say("running" + input.group(1))
#execjs.rule = r'^\.eval\ (.*)$'

if __name__ == '__main__': 
   print __doc__.strip()
   setup();
   run_prompt();