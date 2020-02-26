#!/usr/bin/python3.7

# setup:  enter list in input_lists

from src.libs.setup_log import SetupLogging
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import src.user_inputs.settings_main as settings

import src.user_inputs.address_set as addr_set
import src.user_inputs.address_lists as addr_lists



class Transfer(object):

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

    def transfer(self):      #ch assetid address toaddy pw amt rem
        method_nm = 'transfer'
        base_amt = 2

        amt = base_amt * (10**8)
        #amt = 2000 * (10**8) - 2000
        for receiver in self.receivers:
            print("doing this receiver: ", receiver)
            p_list = [self.chain, self.asset, self.sender, receiver, self.pw, amt, self.remark]
            request = get_top(method_nm, p_list, self.url3)
            resp1 = SendRequest.send_request(request)
            print("resp1: ", resp1)


if __name__ == "__main__":
    c = Transfer()
    c.transfer()

