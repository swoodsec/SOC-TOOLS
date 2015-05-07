#!/usr/bin/python

# Name: Roadie-Shodie - A simple Shodan API search script by Swood.
# Props: Shout out to my daughter Grace!
# Purpose: This script utilizes the Shodan API to search for a user defined term
#          Outputs results to standard out or direct to CSV format.
# Tested: on Python 2.7.6 on OSX, Python 2.7.6 on Debian 7

import shodan
import sys
import csv

# INSERT YOUR API KEY FOR SHODAN BELOW BEFORE RUNNING 
SHODAN_API_KEY = 'INSERT-YOUR-API-KEY-HERE'
api = shodan.Shodan(SHODAN_API_KEY)

# If user hasn't entered API key in this script - Quit!
if SHODAN_API_KEY == 'INSERT-YOUR-API-KEY-HERE':
    print "You must add your API key to this script before running it."
    sys.exit()

# Function declarations.. first function simply prints highly functional banner
def print_banner():
    print " ____ ____ ____ ___  _ ____    ____ _  _ ____ ___  _ ____ "
    print " |__/ |  | |__| |  \ | |___ __ [__  |__| |  | |  \ | |___ "
    print " |  \ |__| |  | |__/ | |___    ___] |  | |__| |__/ | |___ "
    print "Usage: Either supply a search as a command line argument or run with no arguments."

# Function accepts query and searches Shodan API, saving the IP's and data in a dictionary
def shodansearch(query):
# Searching for user query
    try:
        results = api.search(query)
        print 'Total results %s' % results['total']
        for result in results['matches']:
            temp_dict = {result['ip_str']: result['data']}
            shod_dict.update(temp_dict)
    except shodan.APIError, e:
        print 'Error %s' % e
        sys.exit()

# Function prints contents of shodan dictionary, formats with IP: and DATA:
def printsearch(shod_dict):
    for key in shod_dict:
        print 'IP:' + key + '\nDATA:' + shod_dict[key]

def csvoutput(shod_dict):
    # Open/create CSV file for output
    file = csv.writer(open('output.csv', 'wb'))
    for key, value in shod_dict.items():
        file.writerow([key, value])

# Display Banner
print_banner()

# Get user input query if no argument supplied
# If 1 argument is supplied that will be the query
# If more than 2 arguments - display usage
if len(sys.argv) < 2:
    query = raw_input("Shodan Search:")
elif len(sys.argv) == 2:
    query = sys.argv[1]
else:
    print "Usage: Either supply a search as a command line argument or run with no arguments."
    sys.exit()

# Empty dictionary that will hold all data
shod_dict = {}

# Invoke shodansearch with the user's input and print it using printsearch function
shodansearch(query)

# Pick output type and display output
output_type = raw_input("Enter s for Standard Out, or c for CSV")
if output_type == "s":
    printsearch(shod_dict)
elif output_type == "c":
    csvoutput(shod_dict)
else:
    print "Bad input! Start over"
