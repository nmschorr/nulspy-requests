#!/usr/bin/python3.7

import requests
from src.send_req import SendRequest
from src.inputs import Inputs
from src.setup_log import SetupLogging
from src.settings_set import SettingsSet


class Transfer(object):

    def __init__(self):
        SetupLogging()
        settings_d = SettingsSet.settings_set(1)  # 0=KathyUbuntu, 1=westteam
        self.chainId = settings_d.get('chain')
        self.url = settings_d.get('url')
        self.pw = settings_d.get('pw')

        self.head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        self.req = requests.Request('POST', self.url, headers=self.head)
        self.req.json = {"jsonrpc": "2.0"}
        self.remark = "transfer to student account"
        self.id = 99999

    def setup_top(self, method, plist):
        reqr = requests.Request('POST', self.url, headers=self.head)
        reqr.json = {"jsonrpc": "2.0", "method": method, "params": plist, "id": self.id}
        return reqr

    def transfer(self):      #ch assetid address toaddy pw amt rem
        asset = 1
        method_nm = "transfer"
        sender = 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW'
        inputs = Inputs.xferlist

        amt = 2000 * (10**8) - 2000
        for receiver in inputs:
            print("doing this receiver: ", receiver)
            p_list = [self.chainId, asset, sender, receiver, self.pw, amt, self.remark]
            request = self.setup_top(method_nm, p_list)
            resp1 = SendRequest.send_request(request)
            print("resp1: ", resp1)


if __name__ == "__main__":
    c = Transfer()
    c.transfer()

