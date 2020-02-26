#!/usr/bin/python3.7
# a place to put your lists of accounts, etc.

# usage:  from src.user_inputs.input_singles import AddressSingles;  dict = AddressSingles.get_addresses()


def get_addr_set(machine):
    addr_set_d = None
    if machine == 1:
        addr_set_d = {
            'sender': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',

            'sender_pw': 'password123',

            'sender_pw2': 'nuls123456',

            'buyer': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',

            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }

    elif machine == 0:
        addr_set_d = {
            'sender': 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW',

            #'sender_pw': 'password123',

            'sender_pw': 'nuls123456',

            'buyer': 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW',

            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }

    return addr_set_d




        # TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW  kathys
