SOC-TOOLS
=========

This repo is for quick and dirty security analyst tools that I create as needed, hopefully they prove useful! :)

roadie-shodie.py - This script utilizes the Shodan API to search for a user defined term. Outputs results to standard out or direct to CSV format.

ipbulklookup.py - This script takes a list of IP's as input and runs them against a number of open source indicator lists. This is intended as a quick test during an investigation (example: dump the DNS cache or logs from a system under investigation and run this right from your analysis box).

dnsres.py - This is a simple script to do bulk DNS resolution and reverse lookups.

njrat_b64strings.sh - This script takes a pcap file of NJrat C2 traffic as a command line argument and outputs decoded strings from the PCAP in the following format:
==============NJrat PCAP Parser V2.4.5.2.1===================
=========Usage: njrat_b64strings.sh pathtopcap.pcap==========
=========Recommended to direct stdout to a text file=========
=========Malware Config=========
NJ
mybadguyaddress.com:19992
Temp
23524543.exe
False
False
False
False
=========Number of exfiltrated webcam images=========
20
=========Window Titles Viewed=========
My Important Documents
Really important Documents
Really Really important documents
