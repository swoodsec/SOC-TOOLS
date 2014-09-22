#!/bin/python

#Name:          IP Bulk Lookup Tool   
#Description: This script accepts a text file full of IP's (1 per line) and cross references them against a number of live open source lists
# I often find myself in need of a bulk lookup to see if there are blacklist hits in a large IP list (firewall log? access log?). 
# I'll be adding new sources to this as time allows.
#License:        Free as in Free Beer. Please use, abuse and improve :)
#Author:        Andrew Swartwood

# Imports
import urllib2, sets
from sys import argv

# Title and Usage 
print '~~~~ SwoodSec Bulk IP Blacklisterator ~~~~'
print 'Usage: ipbulklookup.py youriplist.txt'

# Open user provided IP list
script, filename = argv
textfile = open(filename)
usertxt = textfile.read()

# Split user input into list
userlist = usertxt.split()

# Download fresh IP blacklists
# Zeus tracker source
zeus = urllib2.urlopen('http://www.abuse.ch/zeustracker/blocklist.php?download=ipblocklist')
# Emerging threats source
emerging = urllib2.urlopen('http://rules.emergingthreats.net/blockrules/compromised-ips.txt')
# Malware Domain List
malware = urllib2.urlopen('http://www.malwaredomainlist.com/hostslist/ip.txt')
# Spyeye tracker source
spyeye = urllib2.urlopen('https://spyeyetracker.abuse.ch/blocklist.php?download=ipblocklist')

# Concat IPs into one variable 'lists'
txtlists = zeus.read() + emerging.read() + malware.read() + spyeye.read()
# Split the sources into an actual list
srclists = txtlists.split()

# Header for matches:
print "IP's in Blacklists (blank if n/a):"

# Find matches between user provided list and blacklists, 
matches = set(userlist) & set(srclists)

# Print matches
for x in matches:
    print x




