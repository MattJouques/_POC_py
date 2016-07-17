#!/usr/bin/python
#
#    POC - Network Connectivity
#
#    @author: Matt Jouques
#

# Configuration

import httplib

conn = httplib.HTTPSConnection("www.google.co.uk")                      # Setup the secure connection 
conn.request("GET", "/")                                                # Connection request
r1 = conn.getresponse()                                                 # Get the page response
data1 = r1.read()                                                       # Get the page content 

print r1.status, r1.reason                                              # Print the response code                                        
print data1                                                             # Print the page content

conn.close()                                                            # Close the connection