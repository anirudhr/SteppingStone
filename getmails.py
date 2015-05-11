#!/usr/bin/python3

import configparser
config = configparser.ConfigParser()
config.read('mailcreds.cfg')
USER = config.get('GMail', 'emailid')
PASS = config.get('GMail', 'password')

import imaplib
server = imaplib.IMAP4_SSL('imap.gmail.com')
server.login(USER, PASS)

from pprint import pprint
pprint(server.list())
