#!/usr/bin/python3.7

import requests
import json
import logging
from src.libs.send_req import SendRequest
from src.user_inputs.inputs import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop


class CreateAccount(object):

    def __init__(self):
        SetupLogging()
        settings_d = SettingsSet.settings_set(1)  # 0=KathyUbuntu, 1=westteam
        self.chainId = settings_d.get('chain')
        self.url = settings_d.get('url')
        self.pw = settings_d.get('pw')

        self.head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        self.req = requests.Request('POST', self.url, headers=self.head)
        self.req.json = {"jsonrpc": "2.0"}
        self.remark = "create account"
        self.id = 99999

    def create_account(self):
        st_obj = SetupTop()
        rg = 19
        for i in range(rg):
            pw = 'password123'
            method_call = "createAccount"
            p_list = [self.chainId, 1, pw]
            request = st_obj.setup_top(method_call, p_list)
            response = SendRequest.send_request(request)

            addr = response[0]
            pri_key = self.get_pri_key(addr)
            response = self.import_pri_key(pri_key)
            bigstr = "\n---created this account: " + addr + "  prikey: " + pri_key + "  pw: " + pw
            print("-----" + bigstr)
            logging.info(bigstr)

    def get_pri_key(self, address):

        pw = 'password123'
        method_call = "getPriKey"
        p_list = [self.chainId, address, pw]
        request = self.setup_top(method_call, p_list)
        pri_key = self.send_request(request)
        print(pri_key)
        return pri_key

    def import_pri_key(self, pri_key):
        pw = 'password123'
        method_call = "importPriKey"
        p_list = [self.chainId, pri_key, pw]
        request = self.setup_top(method_call, p_list)
        result = self.send_request(request)
        # print(result)
        return result

    def check_keys(self):

        cklist = ['TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW']

        for i in cklist:
            key = self.get_pri_key(i)
            bigstr = i + " pk: " + key + " pw: password123"
            print(bigstr)
            logging.info(bigstr)


# "method":"importPriKey",
# "params":[chainId, priKey, password],
# "method":"getPriKey",
# "params":[chainId, address, password],

if __name__ == "__main__":
    c = CreateAccount()
    ####c.create_account()
    # c.check_keys()
    # print(k + " : " + g + " pw: ")
    c.get_pri_key("TTbKRT4jxSikoQMTyZTk5irDyuEX7SM6SUsw")
#  47e9ea04abfcf9e92f91db11726a73a8864b6c1cdd98642c9acf8883855712af
