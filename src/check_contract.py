#!/usr/bin/python3.7

# curl -s -X POST -H -v 'Content-Type: application/json' --data '{"jsonrpc":"2.0",
# "method":"getChainInfo","params":[], "id":1234}' http://78.47.206.255:18003

import requests
import random

class CheckContract(object):

    def __init__(self):
        self.a = 0
        self.url_post = "http://78.47.206.255:18003"
        self.myhead = {"Content-Type": "application/json"}
        chain_id = 24442
        contract_id = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
        self.start_list = [chain_id, contract_id]
        self.chainId = chain_id
        self.contract_id = contract_id
        tup_one = ("jsonrpc", "2.0",)
        self.tup_one = tup_one
        self.rand_id = random.randrange(1, 999)
        self.emp_list = []

    # class data_object(object):
    #     def __init__(self, chain_id, contract_id):
    #         chain_id
    #     start_list = [chain_id, contract_id]
    #     emp_list = []
    #     req_type = "getAllProductIds"
    #     p_str = "() return String"
    #     params_list = [*start_list, req_type, p_str, emp_list]  # 4 items
    #     params = ("params", params_list,)


    def doit(self, params):
        method_type = "invokeView"
        meth_type = ("method", method_type,)

        id_tup = ("id", self.rand_id,)
        req = requests.Request('POST', self.url_post, headers=self.myhead)
        req.json = dict([self.tup_one, meth_type, params, id_tup])
        the_req = req.prepare()
        session = requests.Session()
        rstat = session.send(the_req)
        print("stat: ", rstat)
        the_resp = rstat.text
        print("The response is: %s" % the_resp)
        # return rstat

    def req_basic(self):
        data = {"jsonrpc": "2.0", "method": "getChainInfo", "params": [], "id": 1234}
        req = requests.Request('POST', self.url_post, headers=self.myhead)
        req.json = data
        self.doit(req)

    def req_get_all_prod_ids(self):
        req_type = "getAllProductIds"
        p_str = "() return String"
        params_list = [*self.start_list, req_type, p_str, self.emp_list]  # 4 items
        params = ("params", params_list,)
        self.doit(params)

#curl -s -X POST -H -v "Content-Type: application/json"  --data '{"jsonrpc":"2.0",
# "method":"invokeView","params":[24442,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getReviews","(String productId) return Ljava/util/List;",["baseball"]],"id":914}'  http://78.47.206.255:18003/

    def req_get_reviews(self):
        req_type = "getReviews"
        p_str = "(String productId) return Ljava/util/List;"
        short_list = ["baseball"]  # 4 items
        params_list = [*self.start_list, req_type, p_str, short_list]  # 4 items
        params = ("params", params_list,)
        self.doit(params)

    def req_get_contract(self):
        req_type = "getContract"
        p_str = "(String productId) return Ljava/util/List;"
        arg0 = self.contract_id
        short_list = [arg0]  # 4 items
        params_list = [*self.start_list, req_type, p_str, short_list]  # 4 items
        params = ("params", params_list,)
        self.doit(params)


    #   "raw": "{\n\"jsonrpc\":\"2.0\",\n\"method\":\"getContract\",\n\"params\":[arg0,
    #   arg1],\n\"id\":1234\n}\n"

if __name__ == "__main__":
    c = CheckContract()
    c.req_get_contract()

    print("done")

