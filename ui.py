########################################################################
# Program:
#    Lab 13: Create a cipher
# Author:
#    Br. Helfrich, Kyle Mueller
# Summary: 
#    This program will be able to encrypt and decrypt text using a
#    variety of ciphers.
########################################################################

import cipher, example, cipher01, cipher02, cipher03, cipher04, cipher05, cipher06, cipher07

#####################################################################
# UI CLASS
#####################################################################
class UI:

    #############################################################
    # DEFAULT CONSTRUCTOR
    # sets string to null and loads the cipher list
    #############################################################
    def __init__(self):
        self._cipher = []
        self._plaintext = ""
        self._password = ""

        # load the ciphers into the cipher list
        self._cipher.append(example.Example())   # add the example Cipher
        self._cipher.append(cipher01.Cipher01()) # add 7 other Ciphers
        self._cipher.append(cipher02.Cipher02())
        self._cipher.append(cipher03.Cipher03())
        self._cipher.append(cipher04.Cipher04())
        self._cipher.append(cipher05.Cipher05())
        self._cipher.append(cipher06.Cipher06())
        self._cipher.append(cipher07.Cipher07())

    #############################################################
    # MENU
    # displays the available ciphers and returns the option
    #############################################################
    def menu(self):
        n_options = len(self._cipher)

        # display the options
        print("What cipher do you want to test?\n")
        for i in range(n_options):
            n_cipher = self._cipher[i].get_cipher_name()
            if n_cipher != "cipher name":
                print(f"{i:>4x} .... {n_cipher}")
        
        # get the users option and return it
        return self.get_option(n_options)

    #############################################################
    # GET OPTION
    # prompts for the option and returns the correct index
    #############################################################
    def get_option(self, n_options):
        option = -1

        while option < 0 or option > n_options:
            option = input("> ")

            # check for a value that is not an int
            if not option.isdigit():
                print("ERROR - non-digit entered")

            option = int(option)

            if option < 0 or option > n_options:
                print("ERROR - value is outside the accepted range")

        return option

    #############################################################
    # GET TEXT
    # get the plaintext and password from the user
    #############################################################
    def get_text(self):
        # get the text
        self._plaintext = input("Please enter the text: ")
        if self._plaintext == "":
            self._plaintext = "I am just \"plain\" text."

        # get the password
        self._password = input("Please enter the password: ")
        if self._password == "":
            self._password = "Passw0rd!"
            print(f"Default password: {self._password}")

    #############################################################
    # GET REPORT
    # generates the report for the selected cipher
    #############################################################
    def get_report(self, index):
        encrypted = self._cipher[index].encrypt(self._plaintext, self._password)
        decrypted = self._cipher[index].decrypt(encrypted, self._password)
        print("===================================" \
              "===================================\n" \
              "Cipher Name:         " \
             f"{self._cipher[index].get_cipher_name()}\n" \
              "Pseudocode Author:   " \
             f"{self._cipher[index].get_pseudo_auth()}\n" \
              "Code Encrypt Author: " \
             f"{self._cipher[index].get_encrypt_auth()}\n"
              "Code Decrypt Author: " \
             f"{self._cipher[index].get_decrypt_auth()}\n"
              "===================================" \
              "===================================\n"
              "Citation:\n" \
             f"{self._cipher[index].get_cipher_citation()}\n"
              "===================================" 
              "===================================\n" \
             f"Plain text:    {self._plaintext}\n" \
             f"Cipher text:   {encrypted}\n" \
             f"Decipher text: {decrypted}\n" \
              "===================================" \
              "===================================\n" \
              "Pseudocode:\n" \
             f"{self._cipher[index].get_pseudocode()}")

#####################################################################
# MAIN
# drives the UI class
#####################################################################
def main():
    interface = UI()

    index = interface.menu() # show the menu and get cipher index

    if index == -1: # if index == -1 then quit
        return

    interface.get_text() # get the plaintext and password
    interface.get_report(index) # generate the report

if __name__ == "__main__":
    main()
