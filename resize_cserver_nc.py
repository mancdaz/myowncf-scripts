#!/usr/bin/python

import novaclient 
import ConfigParser

# get our config from the config file
config = ConfigParser.ConfigParser()
config.read("./cf.ini")

USERNAME = config.get("auth", "username")
AUTH_URL = config.get("auth", "url")
API_KEY = config.get("auth", "key")
# Server ID to resize
#SERVER_ID = 10010692

cnx = novaclient.OpenStack(USERNAME, API_KEY, AUTH_URL)
print cnx
cnx.servers.list()
cnx.flavors.list()
