#!/usr/bin/python3.7

# curl -s -X POST -H -v 'Content-Type: application/json' --data '{"jsonrpc":"2.0",
# "method":"getChainInfo","params":[], "id":1234}' http://78.47.206.255:18003

import requests
import random

class PsuSmart(object):

    def __init__(self):
        self.a = 0
        self.url_post = "http://78.47.206.255:18003"
        self.myhead = {"Content-Type": "application/json"}
        chain_id = 24442
        contract_id = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
        self.start_list = [chain_id, contract_id]
        self.chainId = chain_id
        self.contract = contract_id
        tup_one = ("jsonrpc", "2.0",)
        self.tup_one = tup_one
        self.rand_id = random.randrange(1, 999)
        self.emp_list = []


    def doit(self, meth_m, params):
        meth_type = ("method", meth_m,)
        id_tup = ("id", self.rand_id,)
        req = requests.Request('POST', self.url_post, headers=self.myhead)
        req.json = dict([self.tup_one, meth_type, params, id_tup])
        r = req.prepare()
        s = requests.Session()
        rstat = s.send(r)
        print("stat: ", rstat)
        pastebin_url = rstat.text
        print("The response is:%s" % pastebin_url)
        # return rstat

    def req_basic(self):
        data = {"jsonrpc": "2.0", "method": "getChainInfo", "params": [], "id": 1234}
        req = requests.Request('POST', self.url_post, headers=self.myhead)
        req.json = data
        self.doit(req)

    def req_two(self):
        method_m = "invokeView"
        req_type = "getAllProductIds"
        p_str = "() return String"
        params_list = [*self.start_list, req_type, p_str, self.emp_list]  # 4 items
        params = ("params", params_list,)
        self.doit(method_m, params)

#curl -s -X POST -H -v "Content-Type: application/json"  --data '{"jsonrpc":"2.0",
# "method":"invokeView","params":[24442,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getReviews","(String productId) return Ljava/util/List;",["baseball"]],"id":914}'  http://78.47.206.255:18003/

    def req_three(self):
        method_m = "invokeView"
        req_type = "getReviews"
        p_str = "() return String"
        params_list = [*self.start_list, req_type, p_str, self.emp_list]  # 4 items
        params = ("params", params_list,)
        self.doit(method_m, params)


if __name__ == "__main__":
    p = PsuSmart()
    p.req_two()

    print("done")

