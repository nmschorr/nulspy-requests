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
        s = SettingsSet()

        machine = 1   # 1 for west, 0 for kathy

        if machine == 1:
            accts = s.accts_w
            settings = s.settings_w
        else:
            accts = s.accts_k
            settings = s.settings_k

        self.chainId = settings.get('chain')
        self.url = settings.get('url')
        self.pw = settings.get('pw')
        self.sender = accts.get('sender')
        self.remark = "transfer to student account"

        # self.receiver = accts.get('receiver') # get from inputs


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
        st_obj = SetupTop()

        pw = 'contract123'
        method_nm = "getPriKey"
        p_list = [self.chainId, address, pw]
        request = st_obj.setup_top(method_nm, p_list, self.url)
        resp1 = SendRequest.send_request(request)
        print(resp1)
        return resp1

    def import_pri_key(self, pri_key):
        pw = 'password123'
        method_call = "importPriKey"
        p_list = [self.chainId, pri_key, pw]
        request = self.setup_top(method_call, p_list)
        result = self.send_request(request)
        # print(result)
        return result

    def check_keys(self):

        cklist = ['TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk']

        for i in cklist:
            key = self.get_pri_key(i)
            bigstr = i + " pk: " + key
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
    c.get_pri_key("TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk")
#  47e9ea04abfcf9e92f91db11726a73a8864b6c1cdd98642c9acf8883855712af
