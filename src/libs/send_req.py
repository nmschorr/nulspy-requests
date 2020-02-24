#!/usr/bin/python3.7

import requests
import json


class SendRequest(object):

    @staticmethod
    def send_request(req):
        the_request = req.prepare()
        session = requests.Session()
        response = session.send(the_request)
        print(the_request)
        print(response.content)
        data_d = json.loads(response.content)
        return data_d
