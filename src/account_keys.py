#!/usr/bin/python3.7

import logging
from src.libs.setup_log import SetupLogging
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import src.user_inputs.settings_main as settings

import src.user_inputs.address_set as addr_set
import src.user_inputs.address_lists as addr_lists


class AccountKeys(object):

    def __init__(self):
        machine = 0     #   machine = 1   # 1 for west, 0 for kathy
        SetupLogging()
        settings_d = settings.get_settings(machine)
        addr_set_d = addr_set.get_addr_set(machine)

        self.receivers = addr_lists.get_receiver_list()

        self.chain = settings_d.get('chain')
        self.url3 = settings_d.get('url3')
        self.sender = addr_set_d.get('sender')
        self.pw = addr_set_d.get('pw')

        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999

    def get_pri_key(self, pww, address):

        method_nm = "getPriKey"
        p_list = [self.chain, "TTbKRT4o2oSxovbS7xtSauZYtrWFAUsejtti", 'kathy123']
        request = get_top(method_nm, p_list, self.url3)
        resp1 = SendRequest.send_request(request)
        print(resp1)
        # print("chainid: ", self.chain)
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

