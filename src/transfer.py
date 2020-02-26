#!/usr/bin/python3.7

# setup:  enter list in input_lists

from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class Transfer(object):

    def __init__(self):
        machine = 0     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999

    def transfer(self, base_amt):      #ch assetid address toaddy pw amt rem
        method_nm = 'transfer'
        multiplier = 10**8
        amt = base_amt * multiplier
        #amt = 2000 * (10**8) - 2000

        for receiver in self.receivers:
            print("doing this receiver: ", receiver)
            p_list = [self.chain, self.asset, self.sender, receiver, self.pw, amt, self.remark]
            request = get_top(method_nm, p_list, self.url4)
            resp1, rstr = SendRequest.send_request(request)
            print("resp1: ", rstr)


if __name__ == "__main__":
    c = Transfer()
    c.transfer(339)



'''
chainId	int	chain id	yes
assetId	int	asset id	yes
address	string	Transfer out account address	Yes
toAddress	string	Transfer to account address	Yes
password	string	Transfer Account Password	Yes
amount	string	Transfer Amount	Yes
remark	string	Notes	Yes
#return value

'''