#!/usr/bin/env python

"""
Get all files in a cloudfiles container and print
them out - works for containers with >10000 objects
"""

import cloudfiles
import ConfigParser
from sys import argv


# get our config from the config file
config = ConfigParser.ConfigParser()
config.read("./cf.ini")

USERNAME = config.get("auth", "username")
AUTH_URL = config.get("auth", "url")
API_KEY = config.get("auth", "key")

try:
    CONTAINER = argv[1]
    print "Using container: \'%s\'" % CONTAINER
except:
    CONTAINER = "test.birkett"
    print "Using default container: \'%s\'" % CONTAINER

# create the connection object
conn = cloudfiles.get_connection(USERNAME,API_KEY,authurl = AUTH_URL)

# get the container object
container = conn.get_container(CONTAINER)

# print some container details
print  "total size of \'%s\' container: %d bytes" %(container, container.size_used)
print "total number of objects in \'%s\' container: %d" % (container, container.object_count)

# build the list 10000 at a time
last_marker = ''
counter = 0
mainlist = [] 
print "Just populating the list..."
while (counter < container.object_count):
    mylist = container.get_objects(marker=last_marker)
    print "Just grabbing files %d to %d" % (counter, counter + len(mylist))
    counter += 10000
    last_marker = mylist[-1]
    #  extend mainlist by adding current iteration of mylist
    mainlist += mylist

# print the entire main list out
obnum = 1
for object in mainlist:
    print "object number %d: %s" % (obnum, object)
    obnum += 1
