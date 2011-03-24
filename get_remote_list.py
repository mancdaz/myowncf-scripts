#!/usr/bin/env python

"""
Get all files in a cloudfiles container and print
them out - works for containers with >10000 objects
"""

import cloudfiles

USERNAME = "darrenbirkett"
AUTH_URL = "https://lon.auth.api.rackspacecloud.com/v1.0"
API_KEY = "35fcdf2c7ccedff0e257a203d9aaabe1"
#CONTAINER = "testcontainer"
CONTAINER = "test.birkett"

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
