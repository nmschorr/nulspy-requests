#!/usr/bin/python3.7

import requests
import json
from src.libs.send_req import SendRequest
from src.user_inputs.inputs import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop


class CallContract(object):

    def __init__(self):
        SetupLogging()
        s = SettingsSet()
        machine = 0   # 1 for west, 0 for kathy

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
        self.contract_address = accts.get('contract_address')

        # self.receiver = accts.get('receiver') # get from inputs

        self.remark = "transfer to student account"
        self.priceofgas = 25                            # anything 25 or over will work
        self.comment = "a comment"
        self.contract_desc = "(String productId, String reviewComments) return LReviewContract$Review;"

    def get_account_balance(self):
        st_obj = SetupTop()
        method_nm = "getAccountBalance"
        chainid = self.chainId
        p_list = [chainid, chainid, 1, self.sender]
        request = st_obj.setup_top(method_nm, p_list, self.url)
        resp1 = SendRequest.send_request(request)
        # resp = resp1["resp1"]
        print("balance: ", resp1)
        return resp1
                                                    #valueofasset, gaslimit, gas=25
    def call_contract(self, value_asset, args):
        st_obj = SetupTop()
        base_amt = 2
        amt = base_amt * (10**8)
        #amt = 2000 * (10**8) - 2000

        gas_limit = 9900000

        method_nm = "contractCall"
        contract_methodname = "writeReview"
        p_list = [self.chainId, self.sender, self.pw, amt, gas_limit, self.priceofgas,
                  self.contract_address,  contract_methodname, self.contract_desc, args, "my remarks"]
        request = st_obj.setup_top(method_nm, p_list, self.url)
        resp1 = SendRequest.send_request(request)
        results_d = resp1.get("result")
        print(resp1)
        return resp1


if __name__ == "__main__":
    c = CallContract()
    my_review = ["swimsuits", "too large"]
    value_of_asset = 25     # cost to review
    g = c.call_contract(value_of_asset, my_review)
    print(g)
