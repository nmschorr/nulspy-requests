#!/usr/bin/python3.7

import requests
from src.libs.send_req import SendRequest
from src.user_inputs.inputs import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop

class GetBalance(object):
    # http://bin-hex-converter.online-domain-tools.com/

    def __init__(self):
        SetupLogging()
        settings_d = SettingsSet.settings_set(1)   # 0=KathyUbuntu, 1=westteam
        self.chainId = settings_d.get('chain')
        self.url = settings_d.get('url')
        self.pw = settings_d.get('pw')

        self.head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        self.req = requests.Request('POST', self.url, headers=self.head)
        self.req.json = {"jsonrpc": "2.0"}
        self.remark = "get balance"
        self.id = 99999

    def setup_top(self, method, plist):
        reqr = requests.Request('POST', self.url, headers=self.head)
        reqr.json = {"jsonrpc": "2.0", "method": method, "params": plist, "id": self.id}
        return reqr

    def get_account_balance(self):
        st_obj = SetupTop()

        inputs = Inputs.xferlist
        for receiver in inputs:
            method_nm = "getAccountBalance"
            p_list = [self.chainId, self.chainId, 1, receiver]
            request = st_obj.setup_top(method_nm, p_list)
            resp1 = SendRequest.send_request(request)
            results_d = resp1.get("result")

            total_balance = results_d.get("totalBalance")
            balance = results_d.get("balance")
            print("totalBalance: " + receiver + ":  " + str(total_balance))
            #print("     balance: " + receiver + ":  " + str(balance))


if __name__ == "__main__":
    c = GetBalance()
    c.get_account_balance()
