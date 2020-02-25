#!/usr/bin/python3.7

class SettingsSet(object):


    @staticmethod
    def get_settings(chooser) -> dict:
        print("Settings for ", chooser)
        # 0=KathyUbuntu, 1=westteam

        chain_idk = 24442
        urlk3 = "http://78.47.206.255:18003"
        urlk4 = "http://78.47.206.255:18004/jsonrpc"

        # -- # 1  --Westteam = 1
        chain_idw = 4810
        urlw3 = "http://westteam.nulstar.com:18003"
        urlw4 = "http://westteam.nulstar.com:18004/jsonrpc"

        settings_k = {"chain": chain_idk, "url3": urlk3, "url4": urlk4}
        settings_w = {"chain": chain_idw, "url3": urlw3, "url4": urlw4}

        if chooser == 0:  # kathy
            return settings_k
        elif chooser == 1:  # West
            return settings_w
        else:
            print('error')
