#!/usr/bin/python3.7

import requests
import json
import logging
from src.libs.send_req import SendRequest
from src.user_inputs.inputs import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop


class AccountKeys(object):

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

    def get_pri_key(self, pww, address):
        st_obj = SetupTop()

        method_nm = "getPriKey"
        p_list = [self.chainId, "TTbKRT4o2oSxovbS7xtSauZYtrWFAUsejtti", 'kathy123']
        request = st_obj.setup_top(method_nm, p_list, self.url)
        resp1 = SendRequest.send_request(request)
        print(resp1)
        # print("chainid: ", self.chainId)
        # print("address: ", address)
        # print("pww: ", pww)
        return resp1

    def check_keys(self):
        cklist = ['TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk']
        for i in cklist:
            key = self.get_pri_key(i)
            bigstr = i + " pk: " + key
            print(bigstr)
            logging.info(bigstr)




if __name__ == "__main__":
    pw = 'kathy123'
    buyer = 'TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk'
    c = AccountKeys()
    c.get_pri_key(pw, buyer)

