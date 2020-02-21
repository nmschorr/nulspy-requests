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
        senderw = "TTbKRT4kYa7rQXTR3616EsMT6xmPT1pvsris"  #    #TTbKRT4kYa7rQXTR3616EsMT6xmPT1pvsris

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


        # # self.cklist2 = ["TTbKRT4gdnX68zo6NMzt1YoEtcdKUkpdA8SC"]
        #
        # self.cklist = [ 'TTbKRT4h2HMcNMRgWgVxAXzWytSjY5ixrhFW',
        #                 'TTbKRT4hhemTmsv6w9ykeupD6zwu3rC8vpyh']
        #
        # self.cklist3 = ['TTbKRT4iYyndPE7ecCjQKnvaiiUSdiYCXR5E',
        #                 'TTbKRT4kqbSDDSXL2VSE9hvzPoisvKnBoRSz',
        #                 'TTbKRT4mcFGWvCgMwprNVCifkNwgGP7Q2UAv',
        #                 'TTbKRT4mdzsc9dbvMS8N8UUJTCsoxCZTQGue',
        #                 'TTbKRT4mEF6eWHwxUYKaB7qQPuLTGvxWaM6A',
        #                 'TTbKRT4pgb9hUW4JERiuePBSCZNh8zrVQu5o',
        #                 'TTbKRT4rL5dnhRJyYz39VcoftcUDBti9Qrni',
        #                 'TTbKRT4rUxUMvyuBsbfS9PmoHqVJ8EhcRwzD',
        #                 'TTbKRT4rY7bDtZyciJF7dxgsbFzXw7opRzVx',
        #                 'TTbKRT4sYGMwUfocG6qywkoZQMV1dsDbj3JM',
        #                 'TTbKRT4tkrYaRAeQcktSQ5k5voUb35f71feA',
        #                 'TTbKRT4tTAWzAVbsaUwMGqtJnRm2ww6A9U1H',
        #                 'TTbKRT4uidQUHXSAtmNayckjF1pXYyx45M89',
        #                 'TTbKRT4v36STBfA5qA9AHXJfh2i1rtMiN8Xj',
        #                 'TTbKRT4wBXBY4PDqpv4k2Z6cSMR4Lw8R8KsS',
        #                 'TTbKRT4wiwW5EyB5MEhwnv5UoqtkPGoBCmeR',
        #                 'TTbKRT4x17qjDfAZpQwEBNcf7nsccUgs4Vzv',
        #                 'TTbKRT4xMGnUcezcWAjQkHSFUdjrkgxnKZdX']

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
        amt = 2000 * 10**8
        assetid = 1
        for receiver in self.cklist3:
            print("doing this receiver: ", receiver)
            p_list = [self.chainId, assetid, self.sender, receiver, self.pw, amt, self.remark]
            request = self.setup_top(method_nm, p_list)
            resp1 = self.send_request(request)
            print("resp1: ", resp1)


if __name__ == "__main__":
    c = Transfer()
    c.transfer()

