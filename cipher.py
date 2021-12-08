########################################################################
# COMPONENT:
#    CIPHER
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class defines what a cipher is
########################################################################

##################################################
# CIPHER
##################################################
class Cipher:
    def __init__(self):
        pass

    def get_cipher_name(self):
        raise NotImplementedError

    def get_cipher_citation(self):
        raise NotImplementedError

    def get_pseudo_auth(self):
        raise NotImplementedError

    def get_encrypt_auth(self):
        raise NotImplementedError

    def get_decrypt_auth(self):
        raise NotImplementedError

    def get_pseudocode(self):
        raise NotImplementedError

    def encrypt(self, plaintext, password):
        raise NotImplementedError

    def decrypt(self, ciphertext, password):
        raise NotImplementedError