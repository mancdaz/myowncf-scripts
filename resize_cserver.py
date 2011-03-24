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
SERVER_ID = 10010692

cnx = cloudservers.CloudServers(USERNAME, API_KEY, auth_url=AUTH_URL)
cnx.servers.list()

