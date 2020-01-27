#!/usr/bin/python3.7

# curl -s -X POST -H -v 'Content-Type: application/json' --data '{"jsonrpc":"2.0",
# "method":"getChainInfo","params":[], "id":1234}' http://78.47.206.255:18003

# data:{"jsonrpc":"2.0","method":"invokeView","params":[24442,
# "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getRe iews","(String productId) return Ljava/util/List;",["baseballcap"]],"id":904}

# params is first list
# 2nd list is items_list or last_list


#json is:  {'jsonrpc': '2.0', 'method': 'getContract', 'params': [24442, 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM'], 'id': 900032}


import requests
import random
import json


class CheckContract(object):

    def __init__(self):
        self.url_post = "http://78.47.206.255:18003"
        self.myhead = dict([("Content-Type", "application/json",)])
        rand_id = random.randrange(1, 99)
        r_id = 900000 + rand_id
        self.jsonrpc_d = {"jsonrpc": "2.0"}
        #self.id_dict: dict = {"id": rand_id}
        self.id_dict: dict = {"id": r_id}

        chain_id: str = 24442
        self.chainId = chain_id
        contract_id = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
        self.contract_id = contract_id
        self.from_address = "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
        self.write_rev_type = "imputedContractCallGas"
        self.emp_list = []

    def doit(self, method_type, p_list):
        req = requests.Request('POST', self.url_post, headers=self.myhead)

        method_type_tup = {"method": method_type}
        self.jsonrpc_d.update(method_type_tup)

        if method_type == self.write_rev_type:
            param_list = p_list
        elif method_type == "getContract":
            param_list = [self.chainId] + [self.contract_id] + p_list

        else:
            param_list = [self.chainId] + [self.from_address] + p_list

        param_d: dict = {"params": param_list}
        param_d.update(self.id_dict)

        self.jsonrpc_d.update(param_d)
        req.json = self.jsonrpc_d

        print("json is: ", req.json)
        the_req = req.prepare()

        print("the_req is: ", the_req)

        session = requests.Session()
        rstat = session.send(the_req)
        print("stat: ", rstat)
        the_resp = rstat.text
        print("The response is: %s" % the_resp)
        print("\n" + "-------------------")
        # return rstat

    def req_get_chain_info(self):  # uses invoke_view
        method_type = "getChainInfo"
        self.doit(method_type, self.emp_list)

    def req_get_all_prod_ids(self):   # uses invoke_view
        method_type = "invokeView"
        req_type = "getAllProductIds"  # goes in params list
        weird_str = "() return String"
        params_list = [req_type, weird_str, self.emp_list]  # 4 items
        self.doit(method_type, params_list)

            # "method":"invokeView","params":[24442,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getReviews","(String productId) return Ljava/util/List;",["baseball"]],"id":914}'  http://78.47.206.255:18003/
            # "getContract","params":[24442,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"],"id":80}

    def req_get_reviews(self):  # "invokeView"
        method_type = "invokeView"
        request_type = "getReviews"
        weird_str = "(String productId) return Ljava/util/List;"
        last_list = ["baseball"]  # 4 items
        params_list = [request_type, weird_str, last_list]  # 4 items
        self.doit(method_type, params_list)

    # json is: {24442: 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM', 'method': 'invokeView',
    #           'params': ['getReviews', '(String productId) return Ljava/util/List;',
    #                      ['baseball']], 'id': 366}

    def req_get_contract(self):
        method_type = "getContract"
        params_list = []  # 4 items
        self.doit(method_type, params_list)

    # def req_get_info(self):
    #     method_type = "info"
    #     params_list = []  # 4 items
    #     self.doit(method_type, params_list)

    def req_get_writer(self):
        method_type = "getWriter"
        params_list = []  # 4 items
        self.doit(method_type, params_list)

    def write_review(self):
        # cmds.log:POST , path : ,data:{"jsonrpc":"2.0","method":"imputedContractCallGas",
        # "params":[24442,"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",200000000,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
        # "writeReview","(String productId, String reviewComments) return LReviewContract$Review;",["baseball","nice baseball"]],"id":275}

        # write_review is different than the ones above
        sender = self.from_address
        ch_id = self.chainId
        contract_addy = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
        method_dict = "writeReview"
        args = '[{"productId": "baseball"}, {"reviewComments": "happiness"}]"'

        ret_val = "LReviewContract$Review"

        value = '000545454'  # set in stone

        params_list = [ch_id, sender, value, contract_addy, method_dict, ret_val, args]
        self.doit(self.write_rev_type, params_list)


if __name__ == "__main__":
    c = CheckContract()
    c.req_get_all_prod_ids()
    c.req_get_reviews()  ## input contract id, pick product
    c.req_get_contract()
    c.req_get_chain_info()
    c.write_review()
    c.req_get_writer()

    print("done")







#  2, "tNULSeBaMvEtDfvZuukDf2mVyfGo3DdiN8KLRG", 80000000000,
#   "tNULSeBaNA4yaXmfaQVXpX3QWPcUaHRRryoXHa", "multyForAddress", null,
#   [ "tNULSeBaMtkzQ1tH8JWBGZDCmRHCmySevE4frM", "400000000",
#   "tNULSeBaMhKaLzhQh1AhhecUqh15ZKw98peg29", "900000000",
#   "tNULSeBaMv8q3pWzS7bHpQWW8yypNGo8auRoPf", "8045645645" ] ],
#   "id" : 1234

# curl -s -X POST -H -v 'Content-Type:application/json' -d
# {'jsonrpc': '2.0', 'method': 'imputedContractCallGas',
#  'params': [24442, 'TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7', '000545454',
#             'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM', 'writeReview',
#             'LReviewContract$Review',
#             [{"productId":"baseball"}, {"reviewComments":"happiness"}] ], 'id': 900041}
# http://78.47.206.255:18003


'''
The response is:{
   "jsonrpc":"2.0",
   "id":"489",
   "result":{
      "contractAddress":"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
      "creater":"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",
      "createTxHash":"79bb093e7400310627c7fc015392d9df5f0e5b0c6f305c6478dd83c47a3eb373",
      "alias":"nancydemo",
      "blockHeight":312807,
      "success":true,
      "balance":5263800000000,
      "errorMsg":null,
      "tokenType":0,
      "status":0,
      "certificationTime":0,
      "createTime":1579573352,
      "remark":null,
      "txCount":6,
      "deleteHash":null,
      "methods":[
         {
            "name":"<init>",
            "desc":"() return void",
            "returnType":"void",
            "view":false,
            "payable":false,
            "event":false,
            "jsonSerializable":false,
            "params":[

            ]
         },
         {
            "name":"writeReview",
            "desc":"(String productId, String reviewComments) return LReviewContract$Review;",
            "returnType":"LReviewContract$Review;",
            "view":false,
            "payable":true,
            "event":false,
            "jsonSerializable":false,
            "params":[
               {
                  "type":"String",
                  "name":"productId",
                  "required":true
               },
               {
                  "type":"String",
                  "name":"reviewComments",
                  "required":true
               }
            ]
         },
         {
            "name":"getReviews",
            "desc":"(String productId) return Ljava/util/List;",
            "returnType":"Ljava/util/List;",
            "view":true,
            "payable":false,
            "event":false,
            "jsonSerializable":false,
            "params":[
               {
                  "type":"String",
                  "name":"productId",
                  "required":true
               }
            ]
         },
         {
            "name":"getAllProductIds",
            "desc":"() return String",
            "returnType":"String",
            "view":true,
            "payable":false,
            "event":false,
            "jsonSerializable":false,
            "params":[

            ]
         },
         {
            "name":"WriteReviewEvent",
            "desc":"(LReviewContract; var1, String productId, String reviewComments, String writer) return void",
            "returnType":"void",
            "view":false,
            "payable":false,
            "event":true,
            "jsonSerializable":false,
            "params":[
               {
                  "type":"LReviewContract;",
                  "name":"var1",
                  "required":false
               },
               {
                  "type":"String",
                  "name":"productId",
                  "required":false
               },
               {
                  "type":"String",
                  "name":"reviewComments",
                  "required":false
               },
               {
                  "type":"String",
                  "name":"writer",
                  "required":false
               }
            ]
         }
      ],
      "tokenName":null,
      "symbol":null,
      "decimals":0,
      "totalSupply":null,
      "transferCount":0,
      "owners":null,
      "resultInfo":null,
      "args":"[]",
      "new":false,
      "nrc20":false,
      "directPayable":false
   }
}
'''