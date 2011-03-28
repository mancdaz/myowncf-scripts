#!/usr/bin/env python

"""
list all your cf containers
"""

import cloudfiles
import ConfigParser

# get our config from the config file
config = ConfigParser.ConfigParser()
config.read("./cf.ini")

USERNAME = config.get("auth", "username")
AUTH_URL = config.get("auth", "url")
API_KEY = config.get("auth", "key")

# create the connection object
conn = cloudfiles.get_connection(USERNAME,API_KEY,authurl = AUTH_URL)

# create the connection object
conn = cloudfiles.get_connection(USERNAME,API_KEY,authurl = AUTH_URL)

# get a list of containers
containers = conn.get_all_containers()

# print them all out
print "These are all your containers..."
for container in containers:
    print container.name
