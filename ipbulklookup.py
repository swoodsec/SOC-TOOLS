#!/usr/bin/python

#Name:          IP Bulk Lookup Tool   
#Description: This script accepts a text file full of IP's (1 per line) and cross references them against a number of live open source lists
# I often find myself in need of a bulk lookup to see if there are blacklist hits in a large IP list (firewall log? access log?). 
# I'll be adding new sources to this as time allows.
#License:        Free as in Free Beer. Please use, abuse and improve :)
#Author:        Andrew Swartwood

# NOTES: This has been tested on OSX with Python 2.7.5 and Kali Linux with Python 2.7.3. Make sure the text file input contains only one IP per line.

# Imports
from urllib2 import urlopen, HTTPError
import sets
from sys import argv

# Title and Usage 
print '~~~~ SwoodSec Bulk IP Blacklisterator ~~~~'
print 'Usage: ipbulklookup.py youriplist.txt'


if len(argv) > 1:
    # Open user provided IP list
    script, filename = argv
    textfile = open(filename)
    usertxt = textfile.read()

    # Split user input into list
    userlist = usertxt.split()
    
    # Initiating txtlists variable to hold online blacklists.
    txtlists = "Filler"

    # Download fresh IP blacklists
    # Zeus tracker source
    try:
        zeus = urlopen('http://www.abuse.ch/zeustracker/blocklist.php?download=ipblocklist')
    except HTTPError:
        print 'Zeus Tracker not Available'
    else:
        txtlists = txtlists + zeus.read()    
        
    # Emerging threats source
    try:
        emerging = urlopen('http://rules.emergingthreats.net/blockrules/compromised-ips.txt')
    except HTTPError:
        print 'Emerging Threats not Available'
    else:
        txtlists = txtlists + emerging.read()
        
    # Malware Domain List
    try:
        malware = urlopen('http://www.malwaredomainlist.com/hostslist/ip.txt')
    except HTTPError:
        print 'Malware Domain List not Available'
    else:
        txtlists = txtlists + malware.read()
        
    # Spyeye tracker source
    try:
        spyeye = urlopen('https://spyeyetracker.abuse.ch/blocklist.php?download=ipblocklist')
    except HTTPError:
        print 'Spyeye Tracker not Available'
    else:
        txtlists = txtlists + spyeye.read()

    # Concat IPs into one variable 'lists'
    #txtlists = zeus.read() + emerging.read() + malware.read() + spyeye.read()
    # Split the sources into an actual list
    srclists = txtlists.split()

    # Header for matches:
    print "IP's in Blacklists (blank if n/a):"

    # Find matches between user provided list and blacklists, 
    matches = set(userlist) & set(srclists)

    # Print matches
    for x in matches:
        print x
else:
    print 'Requires argument. Please re-run with text file.'
    




