#!/usr/bin/python

import cloudfiles

#USERNAME = "USERNAME"
#API_KEY = "API_KEY"
#AUTH_URL = "https://lon.auth.api.rackspacecloud.com/v1.0"

USERNAME = "darrenbirkett"
AUTH_URL = "https://lon.auth.api.rackspacecloud.com/v1.0"
API_KEY = "35fcdf2c7ccedff0e257a203d9aaabe1"


# create the connection object
conn = cloudfiles.get_connection(USERNAME, API_KEY, authurl = AUTH_URL)

def getandprint_all_containers():
    """ will get a list of containers
    and print them out to stdout"""

    containers = conn.get_all_containers()
    # print them all out
    print "These are all your containers..."
    for container in containers:
        print container.name


# container to delete
getandprint_all_containers()
print "\n"
CONTAINER = raw_input("enter the container name to create: ")

# delete a container

# create a new conntainer
try:
    conn.create_container(CONTAINER)
except:
    print "Failed to create container %s" % CONTAINER
else:
    print "Container %s created successfully" % CONTAINER
    getandprint_all_containers()

