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

        p_list = [self.chainId, asset, 87]
        request = st_obj.setup_top(method_nm, p_list, self.url)
        results_d = SendRequest.send_request(request)
        result = results_d.get("result")
        accts_list = result.get("list")
        for i in accts_list:
            #print(i)
            print(i.get('address'))


if __name__ == "__main__":
    c = GetAccounts()
    c.getaccounts()
