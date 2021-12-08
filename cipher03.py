########################################################################
# COMPONENT:
#    CIPHER 03
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
########################################################################

import cipher

##################################################
# CIPHER 03
##################################################
class Cipher03(cipher.Cipher):
    def __init__(self):
        pass

    def get_pseudo_auth(self):
        return "pseudocode author"

    def get_cipher_name(self):
        return "cipher name"

    def get_encrypt_auth(self):
        return "encrypt author"
    
    def get_decrypt_auth(self):
        return "decrypt author"

    ############################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ############################################################
    def get_cipher_citation(self):
        return "citation"

    ############################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ############################################################
    def get_pseudocode(self):
        # TODO: please format your pseudocode
        # The encrypt pseudocode
        pc = "insert the encryption pseudocode\n"

        # The decrypt pseudocode
        pc += "insert the decryption pseudocode\n"

        return pc

    ############################################################
    # ENCRYPT
    # TODO: ADD description
    ############################################################
    def encrypt(self, plaintext, password):
        ciphertext = plaintext
        # TODO - Add your code here
        return ciphertext

    ############################################################
    # DECRYPT
    # TODO: ADD description
    ############################################################
    def decrypt(self, ciphertext, password):
        plaintext = ciphertext
        # TODO - Add your code here
        return plaintext