#!/usr/bin/python3.7


from src.libs.send_req import SendRequest
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop


class GetAccounts(object):

    def __init__(self):
        machine = 1

        SetupLogging()
        st_obj = SettingsSet()   # 1 for west, 0 for kathy
        settings = st_obj.settings_set(machine)     #   machine = 1   # 1 for west, 0 for kathy

        self.chainId = settings.get('chain')
        self.url = "http://westteam.nulstar.com:18003"

    def getaccounts(self):
        st_obj = SetupTop()
        method_nm = "getAccountList"
        asset = 1

        p_list = [self.chainId, asset, 0]
        request = st_obj.setup_top(method_nm, p_list, self.url)
        resp1 = SendRequest.send_request(request)

        # results_d = resp1.get("result")

        # total_balance = results_d.get("totalBalance")
        print()



if __name__ == "__main__":
    c = GetAccounts()
    c.getaccounts()
