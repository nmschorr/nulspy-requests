#!/usr/bin/python3.7



import requests
import random
import json
from requests.auth import HTTPBasicAuth

class CheckContract(object):

    def __init__(self):
        pass

    def getGas(self):

        url = "http://78.47.206.255:18004/jsonrpc"
        my_id = 99999
        head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        value = 25
        methodk = "imputedContractCallGas"
        method_type_d = {"method": methodk}
        methodName = "writeReview"
        commentk = "a comment"
        req = requests.Request('POST', url, headers=head)
        req.json = {"jsonrpc": "2.0"}
        req.json.update(method_type_d)
        id_dict: dict = {"id": my_id}

        # p_list = [24442, "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7", 25,
        #                    "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM", "writeReview", "writeareview",
        #                    [["swimsuits"], ["too large"]]]
        senderk = "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
        contractAddressk = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
        chainId = 24442

        args = [["swimsuits"], ["too large"]]
        p_list = [chainId, senderk, value, contractAddressk, methodName, commentk, args]

        param_d: dict = {"params": p_list}
        param_d.update(id_dict)
        req.json.update(param_d)
        the_request = req.prepare()
        print("the_req is: ", str(the_request.body))

        session = requests.Session()
        x = session.params
        response = session.send(the_request)
        print(response.content)
        # b'{"jsonrpc":"2.0","id":"99999","result":{"gasLimit":1}}'

        data_d = json.loads(response.content)
        thepair = data_d["result"]
        gas_limit = thepair["gasLimit"]
        print("gas limit: ", gas_limit)
        remark = "a remark"

        # CallContractReq()
        # senderk
        # gas_limit
        # price
        #
        # contractAddressk
        # methodk
        # value
        # args
        # methoddescription
        # remark
        # CallContractReq
        # form = paramsData.get();

        price = 12
        methodDes = "a description"
        meth_desc = "(String productId, String reviewComments) return LReviewContract$Review;"
        args = [["swimsuits"], ["too large"]]
        ccreq = requests.Request('POST', url, headers=head)
        ccreq.json = {"jsonrpc": "2.0"}
        ccreq.json.update(method_type_d)
        id_dict: dict = {"id": my_id}
        pw = "nuls123456"
        p_list = [chainId, senderk, pw, value, gas_limit, price, contractAddressk, methodName, methodDes, args,
                  remark]
        param_d: dict = {"params": p_list}

        param_d.update(id_dict)
        req.json.update(param_d)
        the_request = req.prepare()

        print("the_req is: ", str(the_request.body))

        session = requests.Session()
        x = session.params
        response = session.send(the_request)
        print(response.content)
        # b'{"jsonrpc":"2.0","id":"99999","result":{"gasLimit":1}}'

        data_d = json.loads(response.content)
        thepair = data_d["result"]
        gas_limit = thepair["gasLimit"]
        print("gas limit: ", gas_limit)


        # senderk = "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
        # contractAddressk = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"
        # chainId = 24442




if __name__ == "__main__":
    c = CheckContract()
    g = c.getGas()
    print(g)


# chainId 	int 	chain id 	yes
# sender 	string 	Transaction Creator Account Address 	Yes
# password 	string 	caller account password 	yes
# value 	biginteger 	The amount of the primary network asset that the caller transferred to the contract address. If there is no such service, fill BigInteger.ZERO 	Yes
# gasLimit 	long 	GAS Limit 	Yes
# price 	long 	GAS unit price 	Yes
# contractAddress 	string 	contract address 	yes
# methodName 	string 	contract method 	yes
# methodDesc 	string 	Contract method description, if the method in the contract is not overloaded, this parameter can be empty 	No
# args 	object[] 	List of parameters 	No
# remark 	string 	Transaction Notes 	No
#
{
  "contractAddress": "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
  "createTxHash": "7a2aa78e85cdf37a72e88da25c82acfdff57a5a786718909e2c4d50cc3c45cf5",
  "creater": "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",
  "gasLimit": 11725,
  "price": 25,
  "methodName": "writeReview",
  "methodDesc": "(String productId, String reviewComments) return LReviewContract$Review;",
  "args": "[[\"baseballOutfit\"],[\"fit a little large\"]]",
  "value": 0,
  "resultInfo": {
    "txHash": "7a2aa78e85cdf37a72e88da25c82acfdff57a5a786718909e2c4d50cc3c45cf5",
    "contractAddress": "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
    "success": true,
    "errorMessage": null,
    "result": "{\"productId\":\"baseballOutfit\",\"comments\":\"fit a little large\",\"writer\":\"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7\"}",
    "gasLimit": 11725,
    "gasUsed": 7817,
    "price": 25,
    "totalFee": "0.00393125",
    "txSizeFee": "0.001",
    "actualContractFee": "0.00195425",
    "refundFee": "0.000977",
    "value": "0",
    "nulsTransfers": [],
    "tokenTransfers": [],
    "remark": "call",
    "contractTxList": [],
    "events": [
      "{\"contractAddress\":\"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM\",\"blockNumber\":390697,\"event\":\"WriteReviewEvent\",\"payload\":{\"productId\":\"baseballOutfit\",\"reviewComments\":\"fit a little large\",\"writer\":\"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7\"}}"
    ]
  }
}

