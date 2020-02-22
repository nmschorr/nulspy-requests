#!/usr/bin/python3.7

from src.libs.send_req import SendRequest
from src.user_inputs.inputs import Inputs
from src.libs.setup_log import SetupLogging
from src.user_inputs.settings_set import SettingsSet
from src.libs.setup_top import SetupTop


class Transfer(object):

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
        # self.receiver = accts.get('receiver') # get from inputs

        self.remark = "transfer to student account"
        self.id = 99999

    def transfer(self):      #ch assetid address toaddy pw amt rem
        st_obj = SetupTop()
        method_nm = "transfer"
        asset = 1
        inputs = Inputs.nowlist
        base_amt = 2
        amt = base_amt * (10**8)
        #amt = 2000 * (10**8) - 2000
        for receiver in inputs:
            print("doing this receiver: ", receiver)
            p_list = [self.chainId, asset, self.sender, receiver, self.pw, amt, self.remark]
            settings_w = {"chain": chain_idw, "url": self.url, "pw": pww}
            request = st_obj.setup_top(method_nm, p_list, )
            resp1 = SendRequest.send_request(request)
            print("resp1: ", resp1)


if __name__ == "__main__":
    c = Transfer()
    c.transfer()

