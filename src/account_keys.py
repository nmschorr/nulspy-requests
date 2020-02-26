#!/usr/bin/python3.7

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class AccountKeys(object):

    def __init__(self):
        machine = 0     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
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

