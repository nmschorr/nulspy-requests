#!/usr/bin/python3.7

import requests
from src.libs.send_req import SendRequest
from src.user_inputs.input_lists import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop
from src.user_inputs.addresses_single import AddressSingles;
from src.user_inputs.addresses_single import AddressSingles;


class GetBalance(object):
    # http://bin-hex-converter.online-domain-tools.com/

    def __init__(self):
        machine = 1
        SetupLogging()
        settings_d = SettingsSet().get_settings(machine)  # machine = 1   # 1 for west, 0 for kathy
        singles_d = AddressSingles().get_addresses(machine)

        self.chainId = settings_d.get('chain')
        self.url = "http://westteam.nulstar.com:18003"
        self.sender = singles_d.get('sender')

        self.id = 99999

        self.chainId = settings_d.get('chain')
        self.pw = singles_d.get('pw')
        self.remark = "student account"

    def get_account_balance(self):
        st_obj = SetupTop()

        inputs = Inputs.inputlist
        for receiver in inputs:
            method_nm = "getAccountBalance"
            p_list = [self.chainId, self.chainId, 1, receiver]
            request = st_obj.setup_top(method_nm, p_list, self.url)
            resp1 = SendRequest.send_request(request)
            results_d = resp1.get("result")

            total_balance = results_d.get("totalBalance")
            print("totalBalance: " + receiver + ":  " + str(total_balance))


if __name__ == "__main__":
    c = GetBalance()
    c.get_account_balance()
