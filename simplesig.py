#!/usr/bin/python 

# Name: SimpleSig
# Version: 1.3.37 (revision 1.2)
# Description: Create very simple YARA rules from a keyword list
# Intended Use: Create a YARA rule with keywords for your forensic
# exam to find where these keywords exist in RAM using the "yarascan"
# plugin. This is a very simple string manipulation script that takes
# a text file (one keyword per line) as input and outputs a plaintext 
# YARA signature.

# Tested on OSX && Python 2.7

import sys
import os

# Simple validation that there is a valid text file as command line argument.
if len(sys.argv) < 2:
    print "Please run again with a text file as command line argument."
    sys.exit()
try:
    os.path.isfile(sys.argv[1])
except:
    print "Please run again with a text file as command line argument."
    sys.exit()

# Print banner because importance
print "   _____            __    _____     "   
print "  / __(_)_ _  ___  / /__ / __(_)__ _"
print " _\ \/ /  ' \/ _ \/ / -_)\ \/ / _ `/"
print "/___/_/_/_/_/ .__/_/\__/___/_/\_, / "
print "           /_/               /___/  "
print "------------------------------------"
print "A timesaver for creating very simple YARA"
print '"20% guaranteed to save you 20 seconds!" By: Swood'	
print "------------------------------------"
	
# Request name for finished rule from user.
ruleName = raw_input("#Please enter a name for rule with no spaces:")

outFile = open("%s.yar" % ruleName, "w+")
outFile.write("rule " + ruleName + "\n")
outFile.write("{" + "\n")
outFile.write("    strings:" + "\n")

# Open user provided file in variable
userFile = open(sys.argv[1], "r")

# Read lines into list userKeys
userKeys = userFile.readlines()
# Strip newlines from userKeys Note:NOT WORKING
#for line in userKeys:
#	line.rstrip('\n') 
# Count length of userKeys for use in for loop
wcl = len(userKeys)

# For loop writes the keywords from the text file to YARA strings
# TO DO - this probably won't work out of the box - fix this
for i in range (wcl):
    outFile.write("        $" + str(i) + ' = "' + (userKeys[i]).strip('\n') + '"\n')

outFile.write("    condition: any of them\n")
outFile.write("}\n")





