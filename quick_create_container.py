#!/usr/bin/python

import cloudfiles
import ConfigParser

# get our config from the config file
config = ConfigParser.ConfigParser()
config.read("./cf.ini")

USERNAME = config.get("auth", "username")
AUTH_URL = config.get("auth", "url")
API_KEY = config.get("auth", "key")

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

