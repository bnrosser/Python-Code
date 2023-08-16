# ----------------------------------------------------------------
# Author:  Group 9
#          Brandi Rosser
#          Jaden Fisher
#          Manar Mohammed
# Date:    07/09/2023
#
# This module provides various utility functions.
# -----------------------------------------------------------------

def input_int(prompt):
    # ------------------------------------------------------------
    # This function takes input from the user, then attempts to 
    # convert it to an integer.  It will keep asking until the
    # user's input is valid.
    # It has one parameter:
    # prompt, the message with which to prompt the user.
    # This function returns an integer.
    # -------------------------------------------------------------
    while True:
        result = input(prompt)
        try: return int(result)
        except: print('Please enter an integer.')

def input_string(prompt):
    # ------------------------------------------------------------
    # This function takes input from the user, then validates that
    # it is not an empty string.  It will keep asking until the
    # user's input is valid.
    # It has one parameter:
    # prompt, the message with which to prompt the user.
    # This function returns a non-empty string.
    # -------------------------------------------------------------
    while True:
        result = input(prompt)
        if result != "": return result
        print('Please enter a non-empty string.')

