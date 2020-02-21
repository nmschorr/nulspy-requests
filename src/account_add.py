#!/usr/bin/python3.7

import requests
import json
import logging
import time


class CreateAccount(object):

    def __init__(self):
        machine = 0   # <--- SET MACHINE NUMBER HERE : 0=KathyUbuntu, 1=Westteam

        #-- # -- Westteams's   #0
        chainIdw = 4810   #0
        urlw = "http://westteam.nulstar.com:18004/jsonrpc"

        #-- # -- Kathy's   #1
        chainIdk = 24442
        urlk = "http://78.47.206.255:18004/jsonrpc"

        if machine == 0:  # westteam
            mname = 'Westteam'
            self.chainId = chainIdw
            self.url = urlw
            self.pri = None
        elif machine == 1:  # kathys ubuntu
            mname = 'KathyUbuntu'
            self.chainId = chainIdk
            self.url = urlk
            self.pri = None

        self.head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        self.req = requests.Request('POST', self.url, headers=self.head)
        self.req.json = {"jsonrpc": "2.0"}
        self.comment = "a comment"
        self.id=99999
        ts = time.time()
        tss = str(ts)[:9]
        fname = "..\logs\\acctsCreated" + mname + str(tss) + ".log"
        logging.basicConfig(filename=fname, level=logging.INFO)

    def send_request(self, req):
        response = None
        the_request = req.prepare()
        session = requests.Session()
        # print("the request: ", str(the_request.body))
        #response = session.send(the_request)
        # print(response.content)
        data_d = json.loads(response.content)
        thepair = data_d["result"]
        return thepair

    def setup_top(self, method, plist):
        method_type = {"method": method}
        reqr = requests.Request('POST', self.url, headers=self.head)
        reqr.json = {"jsonrpc": "2.0"}
        reqr.json.update(method_type)
        id_d: dict = {"id": '9999'}
        param_dt: dict = {"params": plist}
        param_dt.update(id_d)
        reqr.json.update(param_dt)
        return reqr

    # "method": "createAccount",
    # "params": [chainId, count, password],
    def create_account(self):
        rg = 1
        for i in range(rg):
            pw = 'password123'
            method_call = "createAccount"
            p_list = [self.chainId, 1, pw]
            request = self.setup_top(method_call, p_list)
            response = self.send_request(request)
            addr = response[0]
            pri_key = self.get_pri_key(addr)
            response = self.import_pri_key(pri_key)
            bigstr = "\n---created this account: " + addr + "  prikey: " + pri_key + "  pw: " + pw
            print("-----" + bigstr)
            logging.info(bigstr)

    def get_pri_key(self, address):

        pw = 'password123'
        method_call = "getPriKey"
        p_list = [self.chainId, address, pw]
        request = self.setup_top(method_call, p_list)
        pri_key = self.send_request(request)
        # print(pri_key)
        return pri_key

    def import_pri_key(self, pri_key):
        pw = 'password123'
        method_call = "importPriKey"
        p_list = [self.chainId, pri_key, pw]
        request = self.setup_top(method_call, p_list)
        result = self.send_request(request)
        # print(result)
        return result

    def check_keys(self):
        mylist = ["TTbKRT4ggekwqyVX2MqbCze8v7gfdban9dFk",
                    "TTbKRT4grYGebwy7TgsPtjHYGr5ZCpgcwc9B",
                    "TTbKRT4hsHgHSufJ4guFFGpWnsArBZFRtRw5",
                    "TTbKRT4ihhbTBeW87ugyMQgxfFbVCznUFh43",
                    "TTbKRT4jNjnK4NgnXuzZbs7p9sTsczZA9qh1",
                    "TTbKRT4jwVBPfM2di6cv5nSqKBeAi54GXWoG",
                    "TTbKRT4jXgGSypSbiS8Mryn7EvoqAxAQkqr4",
                    "TTbKRT4kWZL3LBetgKYGCqGn4zm3FwgvAB3D",
                    "TTbKRT4kYa7rQXTR3616EsMT6xmPT1pvsris",
                    "TTbKRT4m77RHKTFoY46omXemBGBPgVNak1zS",
                    "TTbKRT4nxYfyWgATiHh3dZBrpFe2osT6H21B",
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

        for i in mylist:
            key = self.get_pri_key(i)
            bigstr = i + " pk: " + key + " pw: password123"
            print(bigstr)
            logging.info(bigstr)


# "method":"importPriKey",
# "params":[chainId, priKey, password],
# "method":"getPriKey",
# "params":[chainId, address, password],

if __name__ == "__main__":
    c = CreateAccount()
    # g = c.create_account()
    #k = "TTbKRT4qJ62XeqDC7L5DyHgJwX1Mowsv5LCp"
    g = c.check_keys()
    # print(k + " : " + g + " pw: ")

