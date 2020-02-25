#!/usr/bin/python3.7

import logging
from src.libs.send_req import SendRequest
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop
from src.user_inputs.addresses_single import AddressSingles;


class AccountKeys(object):

    def __init__(self):
        machine = 1
        SetupLogging()
        settings_d = SettingsSet().get_settings(machine)     #   machine = 1   # 1 for west, 0 for kathy
        singles_d = AddressSingles().get_addresses(machine)

        self.chainId = settings_d.get('chain')
        self.url = "http://westteam.nulstar.com:18003"
        self.pw = singles_d.get('pw')
        self.sender = singles_d.get('sender')
        # self.receiver = singles_d.get('receiver') # get from inputs

        self.remark = "transfer to student account"
        self.id = 99999

    def get_pri_key(self, pww, address):
        st_obj = SetupTop()

        method_nm = "getPriKey"
        p_list = [self.chainId, "TTbKRT4o2oSxovbS7xtSauZYtrWFAUsejtti", 'kathy123']
        request = st_obj.setup_top(method_nm, p_list, self.url)
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

