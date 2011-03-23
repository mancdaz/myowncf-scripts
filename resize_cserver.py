#!/usr/bin/python

import cloudservers

USERNAME = "darrenbirkett"
AUTH_URL = "https://lon.auth.api.rackspacecloud.com/v1.0"
API_KEY = "35fcdf2c7ccedff0e257a203d9aaabe1"

# Server ID to resize
SERVER_ID = 10010692

cnx = cloudservers.CloudServers(USERNAME, API_KEY, auth_url=AUTH_URL)



