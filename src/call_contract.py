#!/usr/bin/python3.7

from src.libs.send_req import SendRequest
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_main import SettingsSet
from src.libs.setup_top import SetupTop
from src.user_inputs.address import AddressSingles;


class CallContract(object):

    def __init__(self):
        machine = 1
        SetupLogging()
        settings_d = SettingsSet().get_settings(machine)  # machine = 1   # 1 for west, 0 for kathy
        singles_d = AddressSingles().get_addresses()

        self.chainId = settings_d.get('chain')
        self.url = "http://westteam.nulstar.com:18004/jsonrpc"
        self.pw = singles_d.get('pw')
        self.sender = singles_d.get('sender')

        self.id = 99999

        self.chainId = settings_d.get('chain')
        self.url = settings_d.get('url')
        self.pw = singles_d.get('pw')
        self.remark = "student account"
        self.pw = singles_d.get('pw')
        self.sender = singles_d.get('sender')
        self.contract_address = singles_d.get('contract_address')

        self.remark = "transfer to student account"
        self.priceofgas = 25                            # anything 25 or over will work
        self.comment = "a comment"
        self.contract_desc = "(String productId, String reviewComments) return LReviewContract$Review;"
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
