#!/usr/bin/python3.7

# curl -s -X POST -H -v 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"get_chain_info","params":[], "id":1234}' http://78.47.206.255:18003

# data:{"jsonrpc":"2.0","method":"invokeView","params":[24442,
# "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM","getRe iews","(String productId) return Ljava/util/List;",["baseballcap"]],"id":904}

# params is first list
# 2nd list is items_list or last_list


from src.libs.master_setup import master_setup, unpack_d
from src.libs.setup_top import get_top
from src.libs.send_req import SendRequest


class CheckContract(object):

    def __init__(self):
        machine = 1     #   machine = 1   # 1 for west, 0 for kathy

        settings_d, sender_etc_dd, self.receivers = master_setup(machine)
        self.chain, self.url3, self.sender, self.pw = unpack_d(settings_d, sender_etc_dd)
        self.url4 = settings_d.get('url4')
        self.remark = "transfer to account"
        self.asset = 1
        self.id = 99999
        
        self.emp_list = []

    def doit(self, method_nm, p_list, four=0):   #use url for url4
        if four:
            url = self.url4
        else:
            url = self.url3
        request = get_top(method_nm, p_list, url)
        the_answer = SendRequest.send_request(request)

        print("stat: ", the_answer)
        print("  ANSWER to query ", method_nm, " is: ")
#        print(" ---------> The response is: " + the_answer.text + " ---------> \n\n")
        return the_answer

    def req_get_all_prod_ids(self, contract):   # uses invoke_view
        method_nm = "invokeView"
        method_inner = "getAllProductIds"  # goes in params list
        return_str = "() return String"
        params_list = [self.chain, contract, method_inner, return_str, self.emp_list]  # 4 items
        self.doit(method_nm, params_list)

    def req_get_reviews(self, contract):  # "invokeView"
        method_nm = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        product_list = ["req_get_all_prod_ids"]  # 4 items
        params_list = [self.chain, contract, method_inner,
                       return_val_str, product_list]  # 4
        rlist = self.doit(method_nm, params_list)
        return rlist

    def view_reviews(self, contract):  # "invokeView"
        method_nm = "invokeView"
        method_inner = "getReviews"
        return_val_str = "(String productId) return Ljava/util/List;"
        params_list = [self.chain, contract, method_inner, return_val_str, ["golfball"]]  # 4
        rlist = self.doit(method_nm, params_list)
        return rlist

    def req_get_contract(self, addr):
        method_nm = "getContract"
        params_list = [self.chain, addr]  # 4 items
        self.doit(method_nm, params_list)

    def req_get_writer(self, contract):
        method_nm = "getWriter"
        params_list = [self.chain, contract]  # 4 items
        self.doit(method_nm, params_list)

    def get_account_ledger_list(self, contract):
        method_nm = "getAccountLedgerList"
        p = [self.chain, contract]
        self.doit(method_nm, p)

if __name__ == "__main__":
    c = CheckContract()
    # c.req_get_all_prod_ids()
    # c.req_get_reviews()  ## input contract id, pick product
    # c.req_get_contract()
    ctr = 'TTbKRT5DVddw7rDN1UrS9Wo3xGLFszwYwMLR'
    c.req_get_contract(ctr)
    r = c.view_reviews(ctr)
    print()


# 'params': [{'type': 'String', 'name': 'productId', 'required': True}]},










#  curl -s -X GET -H 'Content-Type: application/json' --data
# http://0.0.0.0:18003/api/account/address/validate  {"chain": 0,"address": "tNULSeBaMmkJbN4ypkbGfhcXdbgjr1HqC2iy8p"}
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
