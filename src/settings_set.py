#!/usr/bin/python3.7

import requests
import json
import logging
import time
from src.send_req import SendRequest
from src.inputs import Inputs
from src.setup_log import SetupLogging

class SettingsSet(object):
    # http://bin-hex-converter.online-domain-tools.com/

    @staticmethod
    def settings_set(machine):
        # 1=KathyUbuntu, 0=westteam
        settings_d = None
        #-- # 0  -- Kathy's Ubuntu = 0
        
        chain_idk = 24442
        urlk = "http://78.47.206.255:18004/jsonrpc"
        # senderk = "TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"
        pwk = 'nuls123456'

        # -- # 1  --Westteam = 1
        chain_idw = 4810
        urlw = "http://westteam.nulstar.com:18004/jsonrpc"
        pww = 'password123'

        if machine == 0:  # kathys ubuntu
            settings_d = {"chain": chain_idk, "url": urlk, "pw": pwk}

        elif machine == 1:  # westteam
            settings_d = {"chain": chain_idw, "url": urlw, "pw": pww}

        return settings_d


  