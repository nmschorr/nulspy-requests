#!/usr/bin/python3.7

# curl -s -X POST -H -v 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"getChainInfo","params":[], "id":1234}' http://78.47.206.255:18003

# data:{"jsonrpc":"2.0","method":"invokeView","params":[24442,
# "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getRe iews","(String productId) return Ljava/util/List;",["baseballcap"]],"id":904}

# params is first list
# 2nd list is items_list or last_list


#json is:  {'jsonrpc': '2.0', 'method': 'getContract', 'params': [24442, 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM'], 'id': 900032}

#works:
# curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc": "2.0", "method": "getAccountLedgerList", "params": [4810, "TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW"], "id": 900008}' http://116.202.157.151:18002
# RPC_METHOD_INVOKER_MAP RPC_METHOD_INVOKER_MAP




import requests
import random
import json
from requests.auth import HTTPBasicAuth

class CheckContract(object):

    def __init__(self):

        which_server = 3

        if which_server == 1:                      # Kathy
            self.url_post  = "http://78.47.206.255:18004/jsonrpc"
            self.owner = "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
            self.contract_address = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
            self.contract_desc =  "(String productId, String reviewComments) return LReviewContract$Review;"
            self.chainId = 24442
            self.senderk = "TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"

        elif which_server == 2:                    # Berzeck Westteam
            self.url_post = "http://116.202.157.151:18003"  # jsonrpc dir?
            #self.url_post = "http://116.202.157.151:18003/jsonrpc"  # jsonrpc dir?
            self.owner = "TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW"
            self.contract_address = "TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW"  #TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW
            self.chainId = 4810

        elif which_server == 3:                                # home Baby
            self.url_post = "http://0.0.0.0:18004/jsonrpc"  # jsonrpc dir?
            self.owner = "tNULSeBaMmkJbN4ypkbGfhcXdbgjr1HqC2iy8p"
            # self.contract_address = "TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW"  #tNULSeBaMmkJbN4ypkbGfhcXdbgjr1HqC2iy8p
            self.chainId = 2


        self.myhead = dict([("Content-Type", "application/json;charset=UTF-8",)])
        rand_id = random.randrange(1, 99)
        r_id = 900000 + rand_id
        self.jsonrpc_d = {"jsonrpc": "2.0"}
        self.id_dict: dict = {"id": r_id}
        self.passwd = "nuls123456"
        self.emp_list = []


#               "(String productId, String reviewComments) return LReviewContract$Review;"
# #               "(String productId, String reviewComments) return LReviewContract$Review;"
#     "TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"
#     sender
#     ["TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"]
#     sender
#     5
#     a020dc9c5110453c4b33608c65c26d6560da007078bb21e94a1022c5333dda8


    def doit(self, method_outer, p_list):

        url = self.url_post
        head = self.myhead
        # authtup = (user, pw)
        #authd = self.auth_d

        req = requests.Request('POST', url, headers=head)

        method_type_d = {"method": method_outer}
        self.jsonrpc_d.update(method_type_d)

        param_d: dict = {"params": p_list}
        param_d.update(self.id_dict)

        #param_d.update(authd)

        self.jsonrpc_d.update(param_d)
        req.json = self.jsonrpc_d

        print("  RUNNING --*--*--* ", str.upper(method_outer), " --*--*--* ")
        print("json is: ", req.json)
        the_request = req.prepare()
        print("the_req is: ", str(the_request.body))

        session = requests.Session()
        x = session.params
        the_answer = session.send(the_request)
        print(the_request.headers)
        print(the_request.url)
        print("stat: ", the_answer)
        print("  ANSWER to query ", method_outer, " is: ")
        print(" ---------> The response is: " + the_answer.text + " ---------> \n\n")

    def req_get_chain_info(self):  # uses invoke_view
        method_outer = "getChainInfo"
        self.doit(method_outer, [self.chainId] )



    def req_get_all_prod_ids(self):   # uses invoke_view
        method_type = "invokeView"
        req_type = "getAllProductIds"  # goes in params list
        weird_str = "() return String"
        params_list = [req_type, weird_str, self.emp_list]  # 4 items
        self.doit(method_type, params_list)


    def req_get_all_prod_ids(self):   # uses invoke_view
        method_outer = "invokeView"
        method_inner = "getAllProductIds"  # goes in params list
        return_str = "() return String"
        params_list = [self.chainId, self.contract_address, method_inner, return_str, self.emp_list]  # 4 items
        self.doit(method_outer, params_list)

            # "method":"invokeView","params":[24442,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getReviews","(String productId) return Ljava/util/List;",["baseball"]],"id":914}'  http://78.47.206.255:18003/
            # "getContract","params":[24442,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"],"id":80}

    def req_get_reviews(self):  # "invokeView"
        method_outer = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        product_list = ["baseball"]  # 4 items
        params_list = [self.chainId, self.contract_address, method_inner,
                       return_val_str, product_list]  # 4
        # items
        self.doit(method_outer, params_list)

    # json is: {24442: 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM', 'method': 'invokeView',
    #           'params': ['getReviews', '(String productId) return Ljava/util/List;',
    #                      ['baseball']], 'id': 366}

    def req_get_contract(self):
        method_outer = "getContract"
        params_list = [self.chainId, self.contract_address]  # 4 items
        self.doit(method_outer, params_list)

    # def req_get_info(self):
    #     method_outer = "info"
    #     params_list = []  # 4 items
    #     self.doit(method_outer, params_list)

    def req_get_writer(self):
        method_outer = "getWriter"
        params_list = [self.chainId, self.contract_address]  # 4 items
        self.doit(method_outer, params_list)

    def write_review(self):
        # cmds.log:POST , path : ,data:{"jsonrpc":"2.0","method":"imputedContractCallGas",
        # "params":[24442,"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",200000000,"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
        #"writeReview","(String productId, String reviewComments) return LReviewContract$Review;",
        # ["baseball","nice baseball"]],"id":275}

        method_outer = "imputedContractCallGas"
        method_inner = "writeReview"
        #args = '[{"productId": "baseball"}, {"reviewComments": "happiness"}]"'
        #params = [{"productId": "baseballshirt2"}, {"reviewComments": "happiness"}]
        params = [{"baseballshirt2": "happiness9777"}]
        p = ["baseballuniformsNew", "they were pretty but and too yellow"]
        ret_val = "(String productId, String reviewComments) return LReviewContract$Review;"

        value = '000545454'  # set in stone
        # value = '700700000'  # set in stone

        params_list = [self.chainId, self.owner, 52400000000, self.contract_address, method_inner,
                       ret_val, p]
        # params_list = [ch_id, sender, value, contract_addy, method_dict, ret_val, params]
        self.doit(method_outer, params_list)

# from web-wallet - perfect!!!!!!!!!!!!!!!!!!!!
# , data: {"jsonrpc": "2.0", "method": "imputedContractCallGas",
#          "params": [24442, "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7", 52400000000,
#                     "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM", "writeReview",
#                     "(String productId, String reviewComments) return LReviewContract$Review;",
#                     ["baseballuniforms", "they were ugly and too small"]], "id": 91}
    def req_do_writer(self):
        method_outer = "WriteReviewEvent"
        rev = "they were pretty but and too yellow"
        item = "baseballsocks"
        p = [self.contract_address, item, rev, self.owner]
        self.doit(self.chainId, p)


    def getTheBestBlock(self):
        method_outer = "getBestBlockHeader"
        p = [ self.chainId ]
        self.doit(method_outer, p)

    def getInfo(self):
        method_outer = "info"
        p = []
        self.doit(method_outer, p)



    # getAccountList
    def getAccountLedgerList(self):
        method_outer = "getAccountLedgerList"
        p = [self.chainId, self.contract_address]
        self.doit(method_outer, p)

    def do_getAccount(self):
        method_outer = "getAddressByPriKey"
        pk = "92dc99194317649ce165e5a8185fc05a751b293c1faf787636adba70e06804c6d5432e5ecc12096c5a3b33a0d6812896"
        p = [pk]
        self.doit(method_outer, p)

    def getAccount1(self):
        method_outer = "getAccount"
        p = [2, "tNULSeBaMmkJbN4ypkbGfhcXdbgjr1HqC2iy8p"]  # Baby
        self.doit(method_outer, p)

    def do_getAddressByPriKey(self):
        method_outer = "getAddressByPriKey"
        pk = "92dc99194317649ce165e5a8185fc05a751b293c1faf787636adba70e06804c6d5432e5ecc12096c5a3b33a0d6812896"
        p = [pk]
        self.doit(method_outer, p)

    def getapi(self):
        method_outer = "getDeclaredMethods"  # requestMethods   getMethods  callCommands  getDeclaredMethods
        p = []
        self.doit(method_outer, p)

    def getaccounts(self):
        method_outer = "getAccounts"
        p = [2]
        self.doit(method_outer, p)

if __name__ == "__main__":
    from time import sleep
    c = CheckContract()
    c.req_get_chain_info()   # easy
    sleep(1)
    # c.req_get_all_prod_ids()
    # c.req_get_reviews()  ## input contract id, pick product
    # c.req_get_contract()
    # c.write_review()
    # c.getAccountLedgerList()
    sleep(1)
    c.do_getAddressByPriKey()
    c.getTheBestBlock()
    sleep(1)
    c.getAccount1()
    sleep(1)
    sleep(1)
    c.getapi()
    c.getaccounts()
    c.do_getAccount


#  curl -s -X GET -H 'Content-Type: application/json' --data
# http://0.0.0.0:18003/api/account/address/validate  {"chainId": 0,"address": "tNULSeBaMmkJbN4ypkbGfhcXdbgjr1HqC2iy8p"}
# @Rpcmethod
# #Rpcmethod
 # curl -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method":"ListAPI", "id": 1234}
    print("done")

# "name": "WriteReviewEvent",
# "desc": "(LReviewContract; var1, String productId, String reviewComments, String writer) return void",
# "returnType": "void",
# "view": false,
# "payable": false,
# "event": true,
# "jsonSerializable": false,
# "params": [
#         {
#                 "type": "LReviewContract;",
#                 "name": "var1",
#                 "required": false
#         },
#         {
#                 "type": "String",
#                 "name": "productId",
#                 "required": false
#         },
#         {
#                 "type": "String",
#                 "name": "reviewComments",
#                 "required": false
#         },
#         {
#                 "type": "String",
#                 "name": "writer",
#                 "required": false


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

#
#
# curl -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "imputedContractCallGas","params": [ 24442,"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7", "545457","TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","writeReview", "LReviewContract$Review", [{"productId": "baseball"}, {"reviewComments": "happiness"}] ], "id": 902755}' -X POST http://78.47.206.255:18003
#
# curl -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "imputedContractCallGas","params": [ 24442,"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7", "545457","TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","writeReview", "LReviewContract$Review", [{"productId": "baseball"}, {"reviewComments": "happiness"}] ], "id": 902755}' -X POST http://78.47.206.255:18003
#
# curl -u "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7":"nuls123456" -H "Content-Type": "application/json" -d '{; "jsonrpc": "2.0",; "method": "imputedContractCallGas",; "params": [; 24442,; "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",; "545457",; "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",; "writeReview",; "LReviewContract$Review",; "[{"productId": "baseball"}, {"reviewComments": "happiness"}]" ],; "id": 902755}' -X POST http://78.47.206.255:18003
#
# curl -H -u "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7":"nuls123456" "Content-Type": "application/json" -d '{; "jsonrpc": "2.0",; "method": "imputedContractCallGas",; "params": [; 24442,; "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",; "545457",; "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",; "writeReview",; "LReviewContract$Review",; "[{"productId": "baseball"}, {"reviewComments": "happiness"}]" ],; "id": 902755}' -X POST http://78.47.206.255:18003
#
#
# {
#   "jsonrpc": "2.0",
#   "id": "900037",
#   "result": {
#     "contractAddress": "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
#     "creater": "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",
#     "createTxHash": "79bb093e7400310627c7fc015392d9df5f0e5b0c6f305c6478dd83c47a3eb373",
#     "alias": "nancydemo",
#     "blockHeight": 312807,
#     "success": true,
#     "balance": 5274200000000,
#     "errorMsg": null,
#     "tokenType": 0,
#     "status": 0,
#     "certificationTime": 0,
#     "createTime": 1579573352,
#     "remark": null,
#     "txCount": 9,
#     "deleteHash": null,
#     "methods": [
#       {
#         "name": "<init>",
#         "desc": "() return void",
#         "returnType": "void",
#         "view": false,
#         "payable": false,
#         "event": false,
#         "jsonSerializable": false,
#         "params": []
#       },
#       {
#         "name": "writeReview",
#         "desc": "(String productId, String reviewComments) return LReviewContract$Review;",
#         "returnType": "LReviewContract$Review;",
#         "view": false,
#         "payable": true,
#         "event": false,
#         "jsonSerializable": false,
#         "params": [
#           {
#             "type": "String",
#             "name": "productId",
#             "required": true
#           },
#           {
#             "type": "String",
#             "name": "reviewComments",
#             "required": true
#           }
#         ]
#       },
#       {
#         "name": "getReviews",
#         "desc": "(String productId) return Ljava/util/List;",
#         "returnType": "Ljava/util/List;",
#         "view": true,
#         "payable": false,
#         "event": false,
#         "jsonSerializable": false,
#         "params": [
#           {
#             "type": "String",
#             "name": "productId",
#             "required": true
#           }
#         ]
#       },
#       {
#         "name": "getAllProductIds",
#         "desc": "() return String",
#         "returnType": "String",
#         "view": true,
#         "payable": false,
#         "event": false,
#         "jsonSerializable": false,
#         "params": []
#       },
#       {
#         "name": "WriteReviewEvent",
#         "desc": "(LReviewContract; var1, String productId, String reviewComments, String writer) return void",
#         "returnType": "void",
#         "view": false,
#         "payable": false,
#         "event": true,
#         "jsonSerializable": false,
#         "params": [
#           {
#             "type": "LReviewContract;",
#             "name": "var1",
#             "required": false
#           },
#           {
#             "type": "String",
#             "name": "productId",
#             "required": false
#           },
#           {
#             "type": "String",
#             "name": "reviewComments",
#             "required": false
#           },
#           {
#             "type": "String",
#             "name": "writer",
#             "required": false
#           }
#         ]
#       }
#     ],
#     "tokenName": null,
#     "symbol": null,
#     "decimals": 0,
#     "totalSupply": null,
#     "transferCount": 0,
#     "owners": null,
#     "resultInfo": null,
#     "args": "[]",
#     "new": false,
#     "nrc20": false,
#     "directPayable": false
#   }
# }
