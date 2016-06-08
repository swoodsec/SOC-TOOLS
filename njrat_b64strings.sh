#!/bin/bash

# This script attempts to summarize a NJrat packet capture. 
# Author: Aswood
# Dependencies: Coreutils (this should work on linux, tested on Ubuntu 14.04)

echo "==============NJrat PCAP Parser V2.4.5.2.1==================="
echo "=========Usage: njrat_b64strings.sh pathtopcap.pcap=========="
echo -e "=========Recommended to direct stdout to a text file=========\n"

# Configuration of malware
echo "=========Malware Config========="
strings $1 | grep "inf" | head -n1 | cut -d"|" -f4 | base64 --decode 

# Webcam summary
echo -e "\n=========Number of exfiltrated webcam images=========" && strings $1 | grep "JFIF" | wc -l

# Windows viewed
echo -e "\n=========Window Titles Viewed=========" 
strings $1 | grep -E "^act" | cut -d"|" -f4 >> tmp.txt
while read i; do echo $i | cut -d"|" -f4 | base64 --decode 2>/dev/null | sort -u ;done<tmp.txt

# Clean-up
rm tmp.txt
