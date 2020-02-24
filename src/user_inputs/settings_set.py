#!/usr/bin/python3.7

class SettingsSet(object):

    def __init__(self):
        self.accts_k = SettingsSet.get_addys_k()
        self.accts_w = SettingsSet.get_addys_w()
        self.settings_k = SettingsSet.settings_set('0')
        self.settings_w = SettingsSet.settings_set('1')

    @staticmethod
    def get_addys_w():   # -- WEST --
        #sender_w = 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW'
        sender_w = 'TTbKRT4jxSikoQMTyZTk5irDyuEX7SM6SUsw'   #password123
        contract_address_w = 'TTbKRT597YGCrQjT6W85ZyP7YiXhA4ZDfJpR'
        receiver_w = 'TTbKRT4nxxnJntdnnwPhFAU6n8VwyJm75nBc'
        accts_w = {'sender': sender_w, 'receiver': receiver_w,
                   'contract_address': contract_address_w}
        return accts_w

    @staticmethod
    def get_addys_k():  # -- Kathy ---
        senderk = "TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"
        receiverk = 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW'
        contract_addressk = 'TTbKRT597YGCrQjT6W85ZyP7YiXhA4ZDfJpR'
        # contractAddressk2 = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"

        accts_k = {'sender': senderk, 'receiver': receiverk,
                   'contract_address': contract_addressk}
        return accts_k

    @staticmethod
    def settings_set(chooser=1):
        settings_d = None

        # 1=KathyUbuntu, 0=westteam

        chain_idk = 24442
        urlk = "http://78.47.206.255:18004/jsonrpc"
        pwk = 'nuls123456'

        # -- # 1  --Westteam = 1
        chain_idw = 4810
        urlw = "http://westteam.nulstar.com:18004/jsonrpc"
        pww = 'password123'

        settings_k = {"chain": chain_idk, "url": urlk, "pw": pwk}
        settings_w = {"chain": chain_idw, "url": urlw, "pw": pww}

        if chooser == '0':  # kathy
            return settings_k
        elif chooser == '1':
            return settings_w
        else:
            print('error')


  