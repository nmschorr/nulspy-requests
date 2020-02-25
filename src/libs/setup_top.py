#!/usr/bin/python3.7

import requests


def get_top(method, plist, url):
    idd = '9999'
    head = dict([("Content-Type", "application/json;charset=UTF-8",)])
    reqr = requests.Request('POST', url, headers=head)
    reqr.json = {"jsonrpc": "2.0", "method": method, "params": plist, "id": idd}
    return reqr
