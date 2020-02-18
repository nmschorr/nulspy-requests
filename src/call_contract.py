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
        contractName = "writeReview"
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
        p_list = [chainId, senderk, value, contractAddressk, contractName, commentk, args]

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


if __name__ == "__main__":
    c = CheckContract()
    g = c.getGas()
    print(g)



