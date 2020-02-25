#!/usr/bin/python3.7

# setup:  enter list in input_lists

from src.libs.send_req import SendRequest
from src.libs.setup_log import SetupLogging
import src.user_inputs.addresses_single as add_sing
from src.user_inputs.input_lists import Inputs
from src.user_inputs.settings_set import get_settings
from src.user_inputs.settings_set import get_settings

from src.libs.setup_top import get_top
import src.user_inputs.settings_set as settings


class Transfer(object):

    def __init__(self):
        machine = 0     #   machine = 1   # 1 for west, 0 for kathy

        SetupLogging()
        settings_d = settings.get_settings(machine)
        singles_d = add_sing.get_singles(machine)
        # self.inputlist = Inputs.inputlist

        self.chain = settings_d.get('chain')
        self.url3 = settings_d.get('url3')
        self.pw = singles_d.get('pw')
        self.sender = singles_d.get('sender')
        # self.receiver = singles_d.get('receiver') # get from inputs

        self.remark = "transfer to account"
        self.id = 99999

    def transfer(self):      #ch assetid address toaddy pw amt rem
        method_nm = 'transfer'
        asset = 1
        base_amt = 2

        amt = base_amt * (10**8)
        #amt = 2000 * (10**8) - 2000
        for receiver in self.inputlist:
            print("doing this receiver: ", receiver)
            p_list = [self.chain, asset, self.sender, receiver, self.pw, amt, self.remark]
            request = get_top(method_nm, p_list, self.url3)
            resp1 = SendRequest.send_request(request)
            print("resp1: ", resp1)


if __name__ == "__main__":
    c = Transfer()
    c.transfer()

