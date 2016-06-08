SOC-TOOLS
=========

This repo is for quick and dirty security analyst tools that I create as needed, hopefully they prove useful! :)

roadie-shodie.py - This script utilizes the Shodan API to search for a user defined term. Outputs results to standard out or direct to CSV format.

ipbulklookup.py - This script takes a list of IP's as input and runs them against a number of open source indicator lists. This is intended as a quick test during an investigation (example: dump the DNS cache or logs from a system under investigation and run this right from your analysis box).

dnsres.py - This is a simple script to do bulk DNS resolution and reverse lookups.

njrat_b64strings.sh - This script takes a pcap file of NJrat C2 traffic as a command line argument and outputs decoded strings from the PCAP for malware config, number of webcam frames exfiltrated, and window titles sent  back to the C2. There is probably a lot of additional functionality of NJrat left to add!
