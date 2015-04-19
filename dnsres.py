#!/usr/bin/python

# DNS and Reverse DNS Resolution Script

# importing socket for "gethostbyname" and "gethostbyaddr"
import socket

# Functions below resolve IP's and URL's one at a time
def resolvedns(inurl):
    return socket.gethostbyname(inurl)
def resolveip(inip):
    return socket.gethostbyaddr(inip)

cont = True

while cont:
# Print title, usage and menu options
    print " __(  _ ( \( ) __)  (  _ ( ___) __)___ "
    print "(___)(_) )  (\__ \   )   /)__)\__ (___)"
    print "   (____(_)\_|___/  (_)\_|____|___/    "
    print "DNS Resolution Script by Swood - Usage ./dnsres.py - View options below"  
    print "Menu:"
    print "a. Resolve Single URL"
    print "b. Resolve Single IP"
    print "c. Resolve File of URLs"
    print "d. Resolve File of IPs" 

# User input for menu selection - Error handling for out of bounds option
    userinput = raw_input("Enter Option:")
    if userinput != "a" and userinput != "b" and userinput != "c" and userinput != "d":
        print "Invalid Option"
        userinput = raw_input("Enter Option:")

# Menu options for IP/URL resolution - Calls resolvedns and resolveip functions

# "a" takes an individual URL and returns the IP address, errors result in a "Unknown host"
    if userinput == "a":
        userurl = raw_input("Enter URL to resolve:")
        userurl = userurl.strip()
        try:
            print resolvedns(userurl)
        except socket.gaierror:
            print "Unknown host"
# "b" takes an individual IP and returns the URL, errors result in a "Unknown host"
    elif userinput == "b":
        userip = raw_input("Enter IP to resolve:")
        userip = userip.strip()
        try:
            print resolveip(userip)
        except socket.gaierror:
            print "Unknown host"
# "c" takes a file path for a list of URLs and turns the IP addresses, errors result in skipping that line in the file (continue)
    elif userinput == "c":
        userfilename = raw_input("Enter file with URL's one per line:")
        userfile = open(userfilename, 'r')
        for line in userfile:
            line = line.strip()
            try:
                print resolvedns(line)
            except socket.gaierror:
                continue
# "d" takes a file path for a list of IPs and turns the URL's, errors result in skipping that line in the file (continue)
    elif userinput == "d":
        userfilename = raw_input("Enter file with IP's one per line:")
        userfile = open(userfilename, 'r')
        for line in userfile:
            line = line.strip()
            try:
                print resolveip(line)
            except socket.gaierror:
                continue
# For everything else, there's mastercard.
    else:
        print "I'm not even sure what you did to get here, please try again."
    
# Ask user if they want to continue
    usercont = raw_input("Enter y to continue:")
    if usercont == "y":
        cont = True
    else:
        cont = False

