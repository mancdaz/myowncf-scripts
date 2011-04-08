#!/usr/bin/python

import cloudservers
import ConfigParser

# get our config from the config file
config = ConfigParser.ConfigParser()
config.read("./cf.ini")

USERNAME = config.get("auth", "username")
AUTH_URL = config.get("auth", "url")
API_KEY = config.get("auth", "key")
# Server ID to resize
SERVER = '10003688' 
FLAVOR = '2'

# create connection object
cnx = cloudservers.CloudServers(USERNAME, API_KEY, auth_url=AUTH_URL)

# get a list of servers on the account
servers = cnx.servers.list()
for server in servers:
    print server 

# get a list of available flavors
flavors = cnx.flavors.list()
for flavor in flavors:
    print flavor

# get a list of server IDs
for server in servers:
    print server.id

# get a list of flavor IDs
for flavor in flavors:
    print flavor.id


# resize specified server
cnx.servers.resize(SERVER, FLAVOR)
cnx.servers.confirm_resize(SERVER)
