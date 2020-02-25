#!/usr/bin/python3.7
# a place to put your lists of accounts, etc.

# usage:  from src.user_inputs.input_singles import AddressSingles;  dict = AddressSingles.get_addresses()


class AddressSingles:

    @staticmethod
    def get_addresses():

        singles = {
            'sender': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',
            'sender_pw': 'password123',
            'sender_pw2': 'nuls123456',
            'buyer': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',
            'receiver': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',
            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }
        return singles

