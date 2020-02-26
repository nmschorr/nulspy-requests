#!/usr/bin/python3.7

import requests


class SendRequest(object):

    @staticmethod
    def send_request(req):
        the_request = req.prepare()
        session = requests.Session()
        response = session.send(the_request)
        print("request is: ", str(the_request.body))
        print()
        return response
