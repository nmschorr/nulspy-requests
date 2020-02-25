#!/usr/bin/python3.7
# a place to put your lists of accounts, etc.

# usage:  from src.user_inputs.input_singles import AddressSingles;  dict = AddressSingles.get_addresses()


def get_singles(machine):
    if machine == 1:
        singles_d = {
            'sender': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',

            'sender_pw': 'password123',

            'sender_pw2': 'nuls123456',

            'buyer': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',

            'receiver': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',

            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }
        return singles_d

    if machine == 0:
        singles_d = {
            'sender': 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW',

            'sender_pw': 'password123',

            # 'sender_pw2': 'nuls123456',

            'buyer': 'TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW',

            'receiver': 'TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7',

            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }
        return singles_d
        # TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW  kathys
