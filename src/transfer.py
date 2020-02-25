#!/usr/bin/python3.7

from src.libs.send_req import SendRequest
from src.user_inputs.input_lists import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop
from src.user_inputs.addresses_single import AddressSingles;


class Transfer(object):

    def __init__(self):
        machine = 1
        SetupLogging()
        settings_d = SettingsSet().get_settings(machine)     #   machine = 1   # 1 for west, 0 for kathy
        singles_d = AddressSingles().get_addresses()

        self.chainId = settings_d.get('chain')
        self.url3 = "http://westteam.nulstar.com:18003"
        self.pw = singles_d.get('pw')
        self.sender = singles_d.get('sender')
        # self.receiver = singles_d.get('receiver') # get from inputs

        self.remark = "transfer to student account"
        self.id = 99999

    def transfer(self):      #ch assetid address toaddy pw amt rem
        st_obj = SetupTop()
        method_nm = 'transfer'
        asset = 1
        base_amt = 2
        inputs = Inputs.inputlist

        amt = base_amt * (10**8)
        #amt = 2000 * (10**8) - 2000
        for receiver in inputs:
            print("doing this receiver: ", receiver)
            p_list = [self.chainId, asset, self.sender, receiver, self.pw, amt, self.remark]
            request = st_obj.setup_top(method_nm, p_list, self.url)
            resp1 = SendRequest.send_request(request)
            print("resp1: ", resp1)


if __name__ == "__main__":
    c = Transfer()
    c.transfer()

