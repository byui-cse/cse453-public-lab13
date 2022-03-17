########################################################################
# COMPONENT:
#    EXAMPLE
# Author:
#    Br. Helfrich, Kyle Mueller
# Summary: 
#    A simple Caesar Cipher to show what your cipher file should contain
########################################################################


##################################################
# EXAMPLE CIPHER
##################################################
class Example:
    def __init__(self):
        # minimum "printable" character
        self._value_minimum = ' '
        # maximum "printable" character
        self._value_maximum = '~'
        # size of alphabet used
        self._size_alphabet = ord(self._value_maximum) \
                              - ord(self._value_minimum) + 1

    def get_author(self):
        return "Brother Helfrich, adapted to Python by Kyle Mueller"

    def get_cipher_name(self):
        return "Caesar Cipher"

    ############################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ############################################################
    def get_cipher_citation(self):
        s = "LearnCryptography.com (2016), " \
            "\"Learn Cryptography - Caesar Cipher\', \n   retrieved: " \
            "https://learncryptography.com/classical-encryption/caesar-cipher"
        return s

    ############################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ############################################################
    def get_pseudocode(self):

        # The encrypt pseudocode
        pc = "encrypt(plainText, password)\n" \
             "   offset <- offsetFromPassword(password)\n" \
             "   FOR p is all values of plainText\n" \
             "      index <- (indexFromCharacter(*p) + offset) % size\n" \
             "      cipherText += characterFromIndex(index)\n" \
             "   RETURN cipherText\n\n"

        # The decrypt pseudocode
        pc += "decrypt(cipherText, password)\n" \
              "   offset <- size - offsetFromPassword(password)\n" \
              "   FOR p is all values of cipherText\n" \
              "      index <- (indexFromCharacter(*p) + offset) % size\n" \
              "      plainText += characterFromIndex(index)\n" \
              "   RETURN plainText\n\n"

        # helper routine
        pc += "offsetFromPassword(password)\n" \
              "   FOR p is all values of password\n" \
              "     offset <- indexFromCharacter(p)\n" \
              "   RETURN offset % size\n"

        return pc

    ############################################################
    # ENCRYPT
    # Shift every value in the plaintext by a fixed amount
    ############################################################
    def encrypt(self, plaintext, password):
        ciphertext = ""
        
        # find a Caesar password from a textual password
        offset = self._offset_from_password(password)
        assert offset >= 0 and offset < self._size_alphabet

        # convert the plaintext one character at a time
        for p in plaintext:
            # convert the character into an index we can work with
            index = self._index_from_character(p)
            
            # perform the shift
            index += offset

            # make sure it is within range
            index %= self._size_alphabet
            assert index >= 0 and index < self._size_alphabet

            # send the index into the ciphertext
            ciphertext += self._character_from_index(index)

        return ciphertext

    ############################################################
    # DECRYPT
    # Shift every value in ciphertext by a fixed amount
    ############################################################
    def decrypt(self, ciphertext, password):
        plaintext = ""
        
        # find a Caesar password from a textual password
        offset = self._offset_from_password(password)
        assert offset >= 0 and offset < self._size_alphabet

        # make the offset backwards
        offset = self._size_alphabet - offset
        assert offset >= 0 and offset < self._size_alphabet

        # convert the ciphertext one character at a time
        for p in ciphertext:
            # convert the character into an index we can work with
            index = self._index_from_character(p)
            
            # perform the shift
            index += offset

            # make sure it is within range
            index %= self._size_alphabet
            assert index >= 0 and index < self._size_alphabet

            # send the index into the ciphertext
            plaintext += self._character_from_index(index)

        return plaintext

    ###################################################
    # INDEX FROM CHARACTER
    # Get an index value from a given letter
    ###################################################
    def _index_from_character(self, letter):
        if letter > self._value_maximum or letter < self._value_minimum:
            return 0
        return ord(letter) - ord(self._value_minimum)

    ###################################################
    # CHARACTER FROM INDEX
    # Get the characer value from a given index
    ###################################################
    def _character_from_index(self, index):
        if index >= 0 and index < self._size_alphabet:
            return chr(index + ord(self._value_minimum))
        return ' '

    ###################################################
    # OFFSET FROM PASSWORD
    # Get the Caesar offset corresponding to a given password
    ###################################################
    def _offset_from_password(self, password):
        offset = 0
        for c in password:
            offset += self._index_from_character(c)
        return offset % self._size_alphabet