#!/usr/bin/python3.7

import requests
import json
import logging
import time

class Transfer(object):
    # http://bin-hex-converter.online-domain-tools.com/

    def __init__(self):
        machine = 1   # 1=KathyUbuntu, 0=westteam

        #-- # 0  -- Kathy's Ubuntu = 0
        chain_idk = 24442
        urlk = "http://78.47.206.255:18004/jsonrpc"
        receiverk = "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
        senderk = "TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"


        pwk = 'nuls123456'

        # -- # 1  --Westteam = 1
        chain_idw = 4810
        urlw = "http://westteam.nulstar.com:18004/jsonrpc"
        receiverw = None
        #senderw = "TTbKRT4kYa7rQXTR3616EsMT6xmPT1pvsris"  #    #TTbKRT4kYa7rQXTR3616EsMT6xmPT1pvsris

        senderw = "TTbKRT4riVan8h5hRJevzt9bJ11FSKuDVGiU"  #    #TTbKRT4kYa7rQXTR3616EsMT6xmPT1pvsris


        pww = 'password123'

        if machine == 0:  # kathys ubuntu
            self.chainId = chain_idk
            self.url = urlk
            self.receiver = receiverk
            self.sender = senderk
            self.pw = pwk
        elif machine == 1:  # westteam
            self.chainId = chain_idw
            self.url = urlw
            self.receiver = receiverw
            self.sender = senderw
            self.pw = pww

        self.head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        self.req = requests.Request('POST', self.url, headers=self.head)
        self.req.json = {"jsonrpc": "2.0"}
        self.remark = "tranfer to student account"
        self.id = 99999

        self.mylist2 = ["TTbKRT4o2Wm5aejgdV3pxC2jVYw5DzGsFzj5"]

        self.cklist = ["TTbKRT4nxYfyWgATiHh3dZBrpFe2osT6H21B",
                        "TTbKRT4o2Wm5aejgdV3pxC2jVYw5DzGsFzj5",
                        "TTbKRT4oNGc58s1K6zw3AUbcfJr9V7SU3WKv",
                        "TTbKRT4ooR8Yb4VgRRitEpDt74qGzo7cNVnQ",
                        "TTbKRT4qYZtALN5vZGHbbNToqTzSTcMJpapL",
                        "TTbKRT4riVan8h5hRJevzt9bJ11FSKuDVGiU",
                        "TTbKRT4sddAQ9j3fVvmvneFA32k1yzfsvC4p",
                        "TTbKRT4sEkWV71GG1D2kTTELyKVrYU3r8J5e",
                        "TTbKRT4taQHeh9XrH7WhzVDu5UM5S2cMEguR",
                        "TTbKRT4tXjJHA9dURtPCDRDfgyQrbdhrmxsy",
                        "TTbKRT4u1cND3XGYg6F2KxACcg6e3uewwJ2y",
                        "TTbKRT4u1KQY4ZUs4qQUetq6mQgTXmTB3Yhh",
                        "TTbKRT4uQxympsoeAZJaadgH8G6CoapZAzG6",
                        "TTbKRT4vzTPhYDqdXCCDJuXUKvPNoTjFqXJm",
                        "TTbKRT4wkUjLYmWeT4faSPWxYdBGtt41AcM3",
                        "TTbKRT4xBpnSBEvVqvbbRRXjPEBAkKnL2XGS",
                        "TTbKRT4o2PPpu3xuKLWCbY1Y6mbmNPB6Gxst",
                        "TTbKRT4oqYmhia4jG8kbBjGzS5Skx59Q94ej",
                        "TTbKRT4vMkq94SLRCZFgRQpQ252SejJQnZrR",
                        "TTbKRT4hTEmtvqcsh6KujDc7ndB4Y3TcPkbY",
                        "TTbKRT4qJ62XeqDC7L5DyHgJwX1Mowsv5LCp"]



        tss = str(time.time())[:9]
        fname = "balanceTransfers" + tss + ".log"
        logging.basicConfig(filename=fname, level=logging.INFO)

    def send_request(self, req):
        the_request = req.prepare()
        session = requests.Session()
        response = session.send(the_request)
        print(response.content)
        data_d = json.loads(response.content)
        thepair = data_d["result"]
        return thepair

    def setup_top(self, method, plist):
        method_type = {"method": method}
        reqr = requests.Request('POST', self.url, headers=self.head)
        reqr.json = {"jsonrpc": "2.0"}
        reqr.json.update(method_type)
        idd: dict = {"id": self.id}
        param_dt: dict = {"params": plist}
        param_dt.update(idd)
        reqr.json.update(param_dt)
        return reqr

    def transfer(self):      #ch assetid address toaddy pw amt rem
        # receiver = "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
        method_nm = "transfer"
        amt = 2000
        assetid = 1
        for receiver in self.mylist2:
            print("doing this receiver: ", receiver)
            p_list = [self.chainId, assetid, self.sender, receiver, self.pw, amt, self.remark]
            request = self.setup_top(method_nm, p_list)
            resp1 = self.send_request(request)
            # resp = resp1["resp1"]
            print("resp1: ", resp1)
            # return resp1

    def get_account_balance(self):
        for receiver in self.cklist:
            method_nm = "getAccountBalance"
            p_list = [self.chainId, self.chainId, 1, receiver]
            request = self.setup_top(method_nm, p_list)
            resp1 = self.send_request(request)
            total_balance = resp1["totalBalance"]
            balance = resp1["balance"]
            print("totalBalance: " + receiver + ":  " + str(total_balance))
            print("     balance: " + receiver + ":  " + str(balance))




if __name__ == "__main__":
    c = Transfer()
    g = c.transfer()
    #g = c.get_account_balance()
    # print(g)

# totalBalance: TTbKRT4o2Wm5aejgdV3pxC2jVYw5DzGsFzj5:  0
#      balance: TTbKRT4o2Wm5aejgdV3pxC2jVYw5DzGsFzj5:  0
# b'{"jsonrpc":"2.0","id":"99999","result":{"totalBalance":"0","balance":"0","timeLock":"0","consensusLock":"0","freeze":"0","nonce":"0000000000000000","nonceType":1}}'
# totalBalance: TTbKRT4oNGc58s1K6zw3AUbcfJr9V7SU3WKv:  0
#      balance: TTbKRT4oNGc58s1K6zw3AUbcfJr9V7SU3WKv:  0
#
#
# totalBalance: TTbKRT4riVan8h5hRJevzt9bJ11FSKuDVGiU:  4000
#      balance: TTbKRT4riVan8h5hRJevzt9bJ11FSKuDVGiU:  4000
# b'{"jsonrpc":"2.0","id":"99999","result":{"totalBalance":"4000","balance":"4000","timeLock":"0","consensusLock":"0","freeze":"0","nonce":"0000000000000000","nonceType":1}}'
# totalBalance: TTbKRT4sddAQ9j3fVvmvneFA32k1yzfsvC4p:  4000
#      balance: TTbKRT4sddAQ9j3fVvmvneFA32k1yzfsvC4p:  4000
# b'{"jsonrpc":"2.0","id":"99999","result":{"totalBalance":"4000","balance":"4000","timeLock":"0","consensusLock":"0","freeze":"0","nonce":"0000000000000000","nonceType":1}}'
# totalBalance: TTbKRT4sEkWV71GG1D2kTTELyKVrYU3r8J5e:  4000
#      balance: TTbKRT4sEkWV71GG1D2kTTELyKVrYU3r8J5e:  4000