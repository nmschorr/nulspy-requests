#!/usr/bin/python3.7

from src.libs.setup_log import SetupLogging
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest
import src.user_inputs.settings_main as settings

import src.user_inputs.address_set as addr_set
import src.user_inputs.address_lists as addr_lists


class GetBalance(object):
    # http://bin-hex-converter.online-domain-tools.com/

    def __init__(self):
        machine = 1
        SetupLogging()
        settings_d = settings.get_settings(machine)
        addr_set_d = addr_set.get_addr_set(machine)
        self.receivers = addr_lists.get_receiver_list()

        self.chain = settings_d.get('chain')
        self.url3 = settings_d.get('url3')

        self.sender = addr_set_d.get('sender')
        self.pw = addr_set_d.get('pw')

        self.remark = "student account"
        self.asset = 1
        self.id = 99999

    def get_account_balance(self):
        method_nm = "getAccountBalance"
        for receiver in self.receivers:
            p_list = [self.chain, self.chain, self.asset, receiver]
            request = get_top(method_nm, p_list, self.url3)
            resp1 = SendRequest.send_request(request)
            results_d = resp1.get("result")

            total_balance = results_d.get("totalBalance")
            print("totalBalance: " + receiver + ":  " + str(total_balance))


if __name__ == "__main__":
    c = GetBalance()
    c.get_account_balance()
