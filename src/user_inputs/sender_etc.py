#!/usr/bin/python3.7
# a place to put your lists of accounts, etc.

# usage:  from src.user_inputs.input_singles import AddressSingles;  dict = AddressSingles.get_addresses()


def get_sender_etc_dict(machine):
    sender_etc_d = None
    if machine == 1:
        sender_etc_d = {
            'sender': 'TTbKRT4vrHMQdyQCATrdu6godeo1FJWSFVVk',

            # 'pw2': 'password123',

            'pw': 'nuls123456',

            'buyer': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z',

            'contract': 'TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z'
            }
#password123

    elif machine == 0:
        sender_etc_d = {
            'sender': 'TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ecZ',

            'pw': 'password123',
            # 'pw2': 'password123',
            #
            # 'pw': 'nuls123456',
            'buyer': 'TTSETeCA3FeQmoc3i8393zZV9WWPU5FmMLQs317',

            'contract': 'TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM' #?
            }

    return sender_etc_d

# TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ecZ  kathys
#TTSETeCA3FeQmoc3i8393zZV9WWPU5FmMLQs317

        # TTbKRT4qEYosbviWgnWLqnMghDWh1CJUgqLW  west?
#TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7
            #'sender_pw': 'password123',
#"TTSETeCA3FWPueNuqEcKUNoxsuKZArhTA7Q2ecZ" kathy's