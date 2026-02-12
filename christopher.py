#!/usr/bin/env python

#\ \  16  21  05  22  06  07  02  03  21  18  05  / /
# \ \ Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee / / 
#  \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /  
#   \      abcd efgh ijkl m-n opqr stuv wxyz     /   
#    \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/    
#    /Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr\    
#    \__________________________________________/    
#          Tool for Encryption & Decryption          
#                 Github: mammaddrik                 

#::::: Library :::::
from lib.banner import Banner
from lib.color import Color, color_banner
from lib.clearscr import clearScr
from lib.slowprint import slowprint

#::::: Detect :::::
from detect.detectenglish import isEnglish

#::::: Src :::::
from src.atbash import atbash
from src.caesar import caesar_encryption, caesar_decryption, caesar_crack
from src.affine import affine_encryption, affine_decryption, affine_crack, extended_gcd
from src.vigenère import vigenère_encrypt, vigenère_decrypt
from src.revers import revers
from src.playfair import massageKey, massageMessage, showgrid, playfair, showres
from src.railfence import railfence_encrypt, railfence_decrypt
from src.scytale import scytale_encrypt, scytale_decrypt
from src.polybiussquare import polybius_square_encrypt, polybius_square_decrypt
from src.columnar import columnar_encrypt, columnar_decrypt
from src.simplesubstitution import simple_substitution_encrypt, simple_substitution_decrypt, generateKey, crack
from src.makewordpatterns import getWordPattern
from src.baconian import baconian_encryption, baconian_decryption
from src.morsecode import morse, morsetext
from src.rot13 import rot13
from src.hashgenerator import hashgenerator
from src.keyboard import Keyboard
from src.plugboard import Plugboard
from src.rotor import Rotor
from src.reflector import Reflector
from src.enigma import Enigma
from src.keygenerator import generateKeys, writeKeysToFile
from src.publickeycipher import publickey_encrypt, publickey_decrypt, readKeysFromFile

#::::: Default Library :::::
import os
import sys
import time
import hashlib
import string
import re
import secrets
from datetime import datetime
from itertools import product
from hmac import compare_digest

#::::: Again :::::
def again():
    "A Function To Ask The User To Restart The Program."
    christopher_again = input(Color.BCyan+"\nDo You Want To Continue?"+Color.End+"\n┌───(christopher)─[~/again]─[Y/n]\n└─"+color_banner[0]+"$ "+Color.End)
    if (christopher_again.upper() == "Y" or christopher_again == ""):
        clearScr()
        time.sleep(0.4)
        christopher()
    elif (christopher_again.upper() == "N"):
        print("\n\tGoodbye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
    else:
        clearScr()
        christopher()

#::::: Keep :::::
def keep():
    "A Function To Ask The User To Decrypt with different keys."
    christopher_keep = input(Color.BCyan+"\nDo You Want To try more keys?"+Color.End+"\n┌───(christopher)─[~/continue]─[Y/n]\n└─"+color_banner[0]+"$ "+Color.End)
    if (christopher_keep.upper() == "Y" or christopher_keep == ""):
        pass
    elif (christopher_keep.upper() == "N"):
        again()
    else:
        again()

#::::: Christopher :::::
def christopher():
    "The function of christoper."
    clearScr()
    print(Banner.cipher_banner)
    choice = input("\n┌───(christopher)─[99]Exit\n└─"+color_banner[0]+"$ "+Color.End)

    #::::: Atbash Cipher :::::
    if (choice == "1" or choice == "01"):
        clearScr()
        print(Banner.banner)
        message = input("\n┌───(christopher)─[Atbash Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
        if len(message) == 0:
            slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
            again()
        elif message.isdigit():
            slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
            again()
        else:
            print(f"└─[Output: {atbash(message)}]")
            again()

    #::::: Caesar Cipher :::::
    elif (choice == "2" or choice == "02"):
        clearScr()
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[Caesar Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if (pick == "1" or pick == "01"):
            clearScr()
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Caesar Cipher/Encryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            elif plaintext.isdigit():
                slowprint("└─["+Color.BRed+"plaintext cannot be only number"+Color.End+"]")
                again()
            try:
                shift = int(input("├─[Enter your shift number]"+color_banner[1]+"$ "+Color.End))
                if shift >= 1 and shift <= 25:
                    print(f"└─[Output: {caesar_encryption(plaintext, shift)}]")
                    again()
                else:
                    slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_encryption(plaintext, shift)}]")
                    again()
            except ValueError:
                slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                shift = 3
                print(f"└─[Output: {caesar_encryption(plaintext, shift)}]")
                again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Caesar Cipher/Decryption]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            elif ciphertext.isdigit():
                slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                again()
            try:
                shift = int(input("├─[Enter your shift number]"+color_banner[1]+"$ "+Color.End))
                if shift >= 1 and shift <= 25:
                    print(f"└─[Output: {caesar_decryption(ciphertext, shift)}]")
                    again()
                else:
                    slowprint("├─["+Color.BRed+"Shift value must be a number Between 1 and 25 (Default: 3)"+Color.End+"]")
                    shift = 3
                    print(f"└─[Output: {caesar_decryption(ciphertext, shift)}]")
                    again()
            except ValueError:
                slowprint("├─["+Color.BRed+"Shift value must be a number (Default: 3)"+Color.End+"]")
                shift = 3
                print(f"└─[Output: {caesar_decryption(ciphertext, shift)}]")
                again()

        #::::: Crack :::::
        elif(pick == "3" or pick == "03"):
            clearScr()
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Caesar Cipher/Crack]\n├─[Enter your Text]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            elif ciphertext.isdigit():
                slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                again()
            decrypted_texts = caesar_crack(ciphertext)
            for i, text in enumerate(decrypted_texts):
                if isEnglish(text):
                    print("├─[Shift: "+Color.BGreen+f"{i+1}"+Color.End+f"]\n└─[The plaintext may be this: {text}]")
                    keep()
            again()

        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Affine Cipher :::::
    elif (choice == "3" or choice == "03"):
        clearScr()
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[Affine Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if (pick == "1" or pick == "01"):
            clearScr()
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Affine Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            elif plaintext.isdigit():
                slowprint("└─["+Color.BRed+"Plaintext cannot be only number"+Color.End+"]")
                again()
            try:
                slope = int(input("├─[Enter your slope(a) number (The number must be odd)]"+color_banner[1]+"$ "+Color.End))
                if slope % 2 == 0:
                    slowprint("└─["+Color.BRed+"Slope(a) value must be a number Between 1 and 25 (The number must be odd)"+Color.End+"]")
                    again()
                intercept = int(input("├─[Enter your intercept(b) number]"+color_banner[1]+"$ "+Color.End))
                if (slope >= 1 and slope <= 25):
                    print(f"└─[Output: {affine_encryption(plaintext, slope, intercept)}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number Between 1 and 25"+Color.End+"]")
                    again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number (Slope(a) number must be odd)"+Color.End+"]")
                again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Affine Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            elif ciphertext.isdigit():
                slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                again()
            try:
                slope = int(input("├─[Enter your slope(a) number (The number must be odd)]"+color_banner[1]+"$ "+Color.End))
                if slope % 2 == 0:
                    slowprint("└─["+Color.BRed+"Slope(a) value must be a number Between 1 and 25 (The number must be odd)"+Color.End+"]")
                    again()
                intercept = int(input("├─[Enter your intercept(b) number]"+color_banner[1]+"$ "+Color.End))
                if (slope >= 1 and slope <= 25):
                    print(f"└─[Output: {affine_decryption(ciphertext, slope, intercept)}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number Between 1 and 25"+Color.End+"]")
                    again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Slope(a) and Intercept(b) value must be a number (Slope(a) number must be odd)"+Color.End+"]")
                again()

        #::::: Crack :::::
        elif(pick == "3" or pick == "03"):
            clearScr()
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Affine Cipher/Crack]\n└─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            elif ciphertext.isdigit():
                slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                again()
            alphabet = string.ascii_lowercase
            m = len(alphabet)
            for a in range(1, m):
                if extended_gcd(a, m)[0] == 1:
                    for b in range(0, m):
                        decrypted_text = affine_crack(ciphertext, a, b)
                        if isEnglish(decrypted_text):
                            print("┌─[Slope(a) = "+Color.BGreen+f"{a} "+Color.End+"Intercept(b) = "+Color.BGreen+f"{b}"+Color.End+f"]\n└─[The plaintext may be this: {decrypted_text}]")
                            keep()
            again()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Vigenère Cipher :::::
    elif (choice == "4" or choice == "04"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[Vigenère Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Vigenère Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if key.isdigit():
                slowprint("└─["+Color.BRed+"Key cannot be number"+Color.End+"]")
                again()
            elif len(key) == 0:
                slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                again()
            key = re.sub(r'\d+', '', key)
            ciphertext = vigenère_encrypt(plaintext, key)
            print(f"└─[Ciphertext: {ciphertext}]")
            again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Vigenère Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).lower().strip()
            plaintext = vigenère_decrypt(ciphertext, key)
            print(f"└─[Plaintext: {plaintext.lower()}]")
            again()

        #::::: Crack :::::
        elif(pick == "3" or pick == "03"):
            clearScr()
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Vigenère Cipher/Crack]\n└─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            character = string.ascii_lowercase
            for i in range(1, 1000):
                for j in product(character, repeat=i):
                    key = "".join(j)
                    key = re.sub(r'\d+', '', key)
                    print(f"├─[Key: {key}]", end='\r')
                    plaintext = vigenère_decrypt(ciphertext, key).upper()
                    if isEnglish(plaintext):
                        print(f"┌─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                        print(f"└─[The plaintext may be this: {plaintext.lower()}]")
                        keep()
            again()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Revers Text :::::
    elif (choice == "5" or choice == "05"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            message = input("\n┌───(christopher)─[Revers Text]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(message) == 0:
                slowprint("└─["+Color.BRed+"message cannot be empty"+Color.End+"]")
                again()
            revers(message)
            again()

    #::::: Playfair Cipher :::::
    elif (choice == "6" or choice == "06"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [99]Back to Main Menu\n\n┌───(christopher)─[Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            enc = True
            usermassage = input("\n┌───(christopher)─[Playfair Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).upper().strip()
            if len(usermassage) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            massage = massageMessage(usermassage)
            user_key = (input("└─[Enter the key]"+color_banner[1]+"$ "+Color.End)+'abcdefghijklmnopqrstuvwxyz').upper()
            key = massageKey(user_key)
            showgrid(key)
            newmassage = playfair(enc,massage,key)
            print('showing digraphs')
            showres(massage, newmassage)
            ciphertext = newmassage
            print(f"[Ciphertext: {ciphertext}]")
            again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            enc = False
            usermassage = input("\n┌───(christopher)─[Playfair Cipher/Decryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).upper().strip()
            if len(usermassage) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            massage = massageMessage(usermassage)
            user_key = (input("└─[Enter the key]"+color_banner[1]+"$ "+Color.End)+'abcdefghijklmnopqrstuvwxyz').upper()
            key = massageKey(user_key)
            showgrid(key)
            newmassage = playfair(enc,massage,key)
            print('showing digraphs')
            showres(massage, newmassage)
            plaintext = newmassage
            print(f"[Plaintext: {plaintext}]")
            again()

        #::::: Back to Main Menu :::::
        elif(pick == "99"):
            christopher()
        else:
            again()

    #::::: Rail Fence Cipher :::::
    elif (choice == "7" or choice == "07"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Rail Fence Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            try:
                key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                if key >= 2 and key <= len(plaintext):
                    ciphertext = railfence_encrypt(plaintext, key)
                    print(f"└─[Ciphertext: {ciphertext}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(plaintext)}"+Color.End+"]")
                    again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Rail Fence Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            try:
                key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                if key >= 2 and key <= len(ciphertext):
                    plaintext = railfence_decrypt(ciphertext, key)
                    print(f"└─[Plaintext: {plaintext}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(plaintext)}"+Color.End+"]")
                    again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                again()

        #::::: Crack :::::
        elif(pick == "3" or pick == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Rail Fence Cipher/Crack]\n└─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            for i in range(2, len(ciphertext)):
                key = i
                plaintext = railfence_decrypt(ciphertext, key).upper()
                if isEnglish(plaintext):
                    print(f"┌─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                    print(f"└─[Plaintext: {plaintext.lower()}]")
                    keep()
            again()

        #::::: Back to Main Menu :::::
        elif(pick == "99"):
            christopher()
        else:
            again()

    #::::: Scytale Cipher :::::
    elif (choice == "8" or choice == "08"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Playfair Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Scytale Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            try:
                diameter = int(input("├─[Enter the diameter number]"+color_banner[1]+"$ "+Color.End))
                ciphertext = scytale_encrypt(plaintext, diameter)
                print(f"└─[Ciphertext: {ciphertext}]")
                again()
            except ValueError:
                slowprint("├─["+Color.BRed+"diameter value must be a number"+Color.End+"]")
                again()

        #::::: Decryption :::::
        if(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Scytale Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            try:
                diameter = int(input("├─[Enter the diameter number]"+color_banner[1]+"$ "+Color.End))
                plaintext = scytale_decrypt(ciphertext, diameter)
                print(f"└─[Ciphertext: {plaintext}]")
                again()
            except ValueError:
                slowprint("├─["+Color.BRed+"diameter value must be a number"+Color.End+"]")
                again()

        #::::: Crack :::::
        if(pick == "3" or pick == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Scytale Cipher/Crack]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            for i in range(2, len(ciphertext)):
                diameter = i
                plaintext = scytale_decrypt(ciphertext, diameter)
                if isEnglish(plaintext):
                    print("├─[Diameter: "+Color.BGreen+f"{i}"+Color.End+f"]\n└─[The plaintext may be this: {plaintext}]")
                    keep()
            again()

        #::::: Back to Main Menu :::::
        elif(pick == "99"):
            christopher()
        else:
            again()

    #::::: Polybius Square Cipher :::::
    elif (choice == "9" or choice == "09"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        message = input("\n┌───(christopher)─[Polybius Square Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper().strip()
        if len(message) == 0:
            slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
            again()
        pick = all(char.isdigit() or char.isspace() for char in message)
        if pick:
            plaintext = polybius_square_decrypt(message)
            print(f"└─[Plaintext: {plaintext.lower()}]")
            again()
        else:
            ciphertext = polybius_square_encrypt(message)
            print(f"└─[Ciphertext: {ciphertext}]")
            again()

        #::::: Columnar Cipher :::::
    elif (choice == "10"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Columnar Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Columnar Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            try:
                key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                if key >= 2 and key <= len(plaintext):
                    ciphertext = columnar_encrypt(plaintext, key)
                    print(f"└─[Ciphertext: {ciphertext}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(plaintext)}"+Color.End+"]")
                    again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                again()
            again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Columnar Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            try:
                key = int(input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End))
                if key >= 2 and key <= len(ciphertext):
                    plaintext = columnar_decrypt(ciphertext, key)
                    print(f"└─[Ciphertext: {plaintext}]")
                    again()
                else:
                    slowprint("└─["+Color.BRed+f"Key value must be a number Between 2 and {len(ciphertext)}"+Color.End+"]")
                    again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Key value must be a number"+Color.End+"]")
                again()

        #::::: Crack :::::
        elif(pick == "3" or pick == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Columnar Cipher/Crack]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            for key in range(1, len(ciphertext)):
                plaintext = columnar_decrypt(ciphertext, key).upper()
                if isEnglish(plaintext):
                    print(f"├─[Key: "+Color.BGreen+f"{key}"+Color.End+"]")
                    print(f"└─[Plaintext: {plaintext.lower()}]")
                    keep()
            again()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Simple Substitution Cipher :::::
    elif (choice == "11"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Crack             [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Simple Substitution Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Simple Substitution Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            elif plaintext.isdigit():
                slowprint("└─["+Color.BRed+"Plaintext cannot be only number"+Color.End+"]")
                again()
            key = generateKey()
            print(f"├─[key: {key}]")
            print(f"└─[Ciphertext: {simple_substitution_encrypt(plaintext, key)}]")
            again()

        #::::: Decryption :::::
        if(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Simple Substitution Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            elif ciphertext.isdigit():
                slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                again()
            key = input(f"├─[Enter your Key]"+color_banner[1]+"$ "+Color.End).strip()
            contains_number = any(char.isdigit() for char in key)
            if contains_number:
                slowprint("└─["+Color.BRed+"The key must be 26 characters without numbers"+Color.End+"]")
                again()
            if len(key) == 26:
                print(f"└─[Plaintext: {simple_substitution_decrypt(ciphertext, key)}]")
                again()
            else:
                slowprint("└─["+Color.BRed+"The key must be 26 characters without numbers"+Color.End+"]")
                again()

        #::::: Crack :::::
        if(pick == "3" or pick == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[Simple Substitution Cipher/Crack]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            elif ciphertext.isdigit():
                slowprint("└─["+Color.BRed+"Ciphertext cannot be only number"+Color.End+"]")
                again()
            patterns = input("├─[Do you have a Word Pattern file]─[Y/n]"+color_banner[1]+"$ "+Color.End).strip()
            if (patterns.upper() == "Y" or patterns == ""):
                crack(ciphertext)
                again()
            elif (patterns.upper() == "N"):
                wordPatterns = {}
                file = input("├─[Enter the file]"+color_banner[1]+"$ "+Color.End).strip()
                try:
                    with open(file, "r") as f:
                        filesize = os.path.getsize((pwfile))
                        if filesize == 0:
                            slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                            again()
                except FileNotFoundError:
                    slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                    again()
                path = os.getcwd()
                if os.name == "nt":
                    with open(file, "r") as f:
                        for word in f:
                            word = word.strip()
                            pattern = getWordPattern(word)
                            if pattern in wordPatterns:
                                wordPatterns[pattern].append(word)
                            else:
                                wordPatterns[pattern] = [word]
                        with open(path+"/src/wordpatterns.py", "w") as f:
                            f.write(f"wordPatterns = {wordPatterns}")
                else:
                    try:
                        with open(path+"/src/wordpatterns.py", "w") as f:
                            f.write(f"wordPatterns = {wordPatterns}")
                    except FileNotFoundError:
                        dictionaryFile = open(path+'/src/wordpatterns.py')
                crack(ciphertext)
                again()
            else:
                again()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Baconian Cipher :::::
    elif (choice == "12"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        message = input("\n┌───(christopher)─[Baconian Cipher]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper().strip()
        if len(message) == 0:
            slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
            again()
        elif message.isdigit():
            slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
            again()
        elif re.fullmatch(r'[AB]*', message):
            chunk_size = 5
            print(f"└─[Plaintext: ", end='')
            for i in range(0, len(message), chunk_size):
                decoded = baconian_decryption(message[i:i + chunk_size])
                print(f"{decoded.lower()}",end='')
            print("]")
            again()
        else:
            print(f"└─[Ciphertext: {baconian_encryption(message)}]")
            again()

    #::::: Morse Code :::::
    elif (choice == "13"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        message = input("\n┌───(christopher)─[Morse Code]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper()
        if len(message) == 0:
            slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
            again()
        elif message.isdigit():
            slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
            again()
        characters = {'-', '.', ' '}
        pick = all(char in characters for char in message)
        if pick:
            morsetext(message)
            again()
        else:
            morse(message)
            again()

    #::::: Rot13 Cipher :::::
    elif (choice == "14"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        message = input("\n┌───(christopher)─[Rot13]\n├─[Enter your text]"+color_banner[1]+"$ "+Color.End).lower().strip()
        if len(message) == 0:
            slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
            again()
        elif message.isdigit():
            slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
            again()
        else:
            print(f"└─[Output: {rot13(message)}]")
            again()

    # One-Time Pad Cipher
    elif (choice == "15"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/One-Time Pad Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[One-Time Pad Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            SYMBOLS = string.ascii_letters
            key = ""
            for i in range(len(plaintext)):
                key += secrets.choice(SYMBOLS)
            print(f"├─[Key: {key}]")
            ciphertext = vigenère_encrypt(plaintext, key)
            print(f"└─[Ciphertext: {ciphertext}]")
            again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            ciphertext = input("\n┌───(christopher)─[One-Time Pad Cipher/Decryption]\n├─[Enter your Ciphertext]"+color_banner[1]+"$ "+Color.End).lower().strip()
            if len(ciphertext) == 0:
                slowprint("└─["+Color.BRed+"Ciphertext cannot be empty"+Color.End+"]")
                again()
            key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).lower().strip()
            plaintext = vigenère_decrypt(ciphertext, key)
            print(f"└─[Plaintext: {plaintext.lower()}]")
            again()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Hash Function :::::
    elif (choice == "16"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Hash Generator     [02]Hash Cracker\n   [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Hash Function]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Hash Generator :::::
        if (pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            password = input("\n┌───(christopher)─[Hash Function/Hash Generator]\n├─[Enter the password]"+color_banner[1]+"$ "+Color.End).strip()
            if len(password) == 0:
                slowprint("└─["+Color.BRed+"Password cannot be empty"+Color.End+"]")
                again()
            hashvalue = input("├───────────────┬───────────────┬───────────────┐\n├─[01]MD2       ├─[2]MD4        ├─[03]MD5       │\n├─[04]SHA1      ├─[05]SHA224    ├─[06]SHA256    │\n├─[07]SHA384    ├─[08]SHA512    ├─[09]sha3-224  │\n├─[10]sha3-256  ├─[11]sha3-384  ├─[12]sha3-512  │\n├─[13]shake-128 ├─[14]shake-256 ├─[15]blake2b   │\n├─[16]blake2s   ├─[17]NTLM      ├─[18]adler32   │\n├─[19]crc32     ├─[20]all       ├─[21]Back      │\n├───────────────┴───────────────┴───────────────┘\n└─[Select the function]"+color_banner[1]+"$ "+Color.End)
            if len(hashvalue) == 0:
                slowprint("└─["+Color.BRed+"Hashvalue cannot be empty"+Color.End+"]")
                again()
            if (hashvalue == "1" or hashvalue == "01"):
                hashvalue = "md2"
            elif (hashvalue == "2" or hashvalue == "02"):
                hashvalue = "md4"
            elif (hashvalue == "3" or hashvalue == "03"):
                hashvalue = "md5"
            elif (hashvalue == "4" or hashvalue == "04"):
                hashvalue = 'sha1'
            elif (hashvalue == "5" or hashvalue == "05"):
                hashvalue = 'sha224'
            elif (hashvalue == "6" or hashvalue == "06"):
                hashvalue = 'sha256'
            elif (hashvalue == "7" or hashvalue == "07"):
                hashvalue = 'sha384'
            elif (hashvalue == "8" or hashvalue == "08"):
                hashvalue = 'sha512'
            elif (hashvalue == "9" or hashvalue == "09"):
                hashvalue = 'sha3_224'
            elif (hashvalue == "10"):
                hashvalue = 'sha3_256'
            elif (hashvalue == "11"):
                hashvalue = 'sha3_384'
            elif (hashvalue == "12"):
                hashvalue = 'sha3_512'
            elif (hashvalue == "13"):
                hashvalue = 'shake_128'
            elif (hashvalue == "14"):
                hashvalue = 'shake_256'
            elif (hashvalue == "15"):
                hashvalue = 'blake2b'
            elif (hashvalue == "16"):
                hashvalue = 'blake2s'
            elif (hashvalue == "17"):
                hashvalue = 'NTLM'
            elif (hashvalue == "18"):
                hashvalue = 'adler32'
            elif (hashvalue == "19"):
                hashvalue = 'crc32'
            elif (hashvalue == "20"):
                hashvalue = 'all'
            elif (hashvalue == "21"):
                christopher()
            else:
                slowprint("└─["+Color.BRed+"Enter the Available Function"+Color.End+"]")
                again()
            hashgenerator(password, hashvalue)
            again()

        #::::: Hash Cracker :::::
        elif (pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            Hash = input("\n┌───(christopher)─[Hash Function/Hash Cracker]\n├─[Enter the hash]"+color_banner[1]+"$ "+Color.End).strip()
            if len(Hash) == 32:
                hashvalue = "md5"
            elif len(Hash) == 40:
                hashvalue = "sha1"
            elif len(Hash) == 64:
                hashvalue = "sha256"
            elif len(Hash) == 96:
                hashvalue = "sha384"
            elif len(Hash) == 128:
                hashvalue = "sha512"
            else:
                slowprint("└─["+Color.BRed+"Hash Function: Unknown"+Color.End+"]")
                again()
            pick = input("├─[Do you have a passwordlist]─[Y/n]"+color_banner[1]+"$ "+Color.End)
            if (pick.upper() == "Y" or pick == ""):
                pwfile = input("├─[Enter the password file name]"+color_banner[1]+"$ "+Color.End)
                try:
                    with open(pwfile, "r") as f:
                        filesize = os.path.getsize((pwfile))
                        if filesize == 0:
                            slowprint("└─["+Color.BRed+"File is Empty"+Color.End+"]")
                            again()
                    with open(pwfile, "r") as f:
                        counter = 1
                        t1 = datetime.now()
                        for password in f:
                            h = hashlib.new(hashvalue)
                            setpass = bytes(password.strip(), "utf-8")
                            h.update(setpass)
                            hashedguess = h.hexdigest()
                            counter += 1
                            print(f"├─[Password number {counter}: {password.strip()}]")
                            if compare_digest(Hash, hashedguess):
                                t2 = datetime.now()
                                t3 = t2 - t1
                                print(f"├─[Finishing Time: {t3}]")
                                print("└─[Password: "+Color.BGreen+f"{password.strip()}"+Color.End+"]")
                                again()
                        else:
                            slowprint("└─["+Color.BRed+"Password Not Found"+Color.End+"]")
                            again()
                except FileNotFoundError:
                    slowprint("└─["+Color.BRed+"File Not Found"+Color.End+"]")
                    again()
                except OSError:
                    slowprint("└─["+Color.BRed+"File Not Found Check the filename"+Color.End+"]")
                    again()
            elif (pick.upper() == "N"):
                counter = 0
                character = string.ascii_letters+string.digits+string.punctuation
                t1 = datetime.now()
                for i in range(1, 1000):
                    for j in product(character, repeat=i):
                        word = "".join(j)
                        h = hashlib.new(hashvalue)
                        setpass = bytes(word.strip(), "utf-8")
                        h.update(setpass)
                        hashedguess = h.hexdigest()
                        counter += 1
                        print(f"├─[Password number {counter}: {word.strip()}]", end='\r')
                        if compare_digest(Hash, hashedguess):
                            t2 = datetime.now()
                            t3 = t2 - t1
                            print(f"├─[Password number {counter}: {word.strip()}]")
                            print(f"├─[Finishing Time: {t3}]")
                            print("└─[Password: "+Color.BGreen+f"{word}"+Color.End+"]")
                            again()
                else:
                    slowprint("└─["+Color.BRed+"Password Not Found"+Color.End+"]")
                    again()
            else:
                clearScr()
                christopher()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Enigma Machine :::::
    elif (choice == "17"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
        II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
        III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
        IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
        V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
        A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
        B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
        KB = Keyboard()
        PB = Plugboard(["PI", "KM", "JB", "YU", "QS", "ZA", "GW", "CH", "XF"])
        ENIGMA = Enigma(A, III, II, IV, PB, KB)
        ENIGMA.set_rings((22,2,6))
        message = input("\n┌───(christopher)─[Enigma Machine]\n├─[Enter your message]"+color_banner[1]+"$ "+Color.End).upper().strip()
        if len(message) == 0:
            slowprint("└─["+Color.BRed+"Message cannot be empty"+Color.End+"]")
            again()
        elif message.isdigit():
            slowprint("└─["+Color.BRed+"Message cannot be only number"+Color.End+"]")
            again()
        message = ''.join(c for c in message if c.isalpha() or c.isspace())
        key = input("├─[Enter the key]"+color_banner[1]+"$ "+Color.End).upper().strip()
        if len(key) == 0:
            slowprint("└─["+Color.BRed+"Key cannot be empty"+Color.End+"]")
            again()
        elif key.isdigit():
            slowprint("└─["+Color.BRed+"Key cannot be only number"+Color.End+"]")
            again()
        key = ''.join(c for c in key if c.isalpha() or c.isspace())
        if len(key) == 3:
            ENIGMA.set_key(key)
            ciphertext = ""
            for letter in message:
                ciphertext = ciphertext + ENIGMA.encipher(letter)
            print(f"└─[Output: {ciphertext}]")
            again()
        else:
            slowprint("└─["+Color.BRed+"The key must be exactly three characters long."+Color.End+"]")
            again()

    #::::: Public Key Cipher :::::
    elif (choice == "18"):
        clearScr()
        time.sleep(0.4)
        print(Banner.banner)
        pick = input("   [01]Encryption        [02]Decryption\n   [03]Key Generator     [99]Back to Main Menu\n\n┌───(christopher)─[~/christopher/Cryptography/Public Key Cipher]\n└─"+color_banner[1]+"$ "+Color.End)

        #::::: Encryption :::::
        if(pick == "1" or pick == "01"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            plaintext = input("\n┌───(christopher)─[Public Key Cipher/Encryption]\n├─[Enter your Plaintext]"+color_banner[1]+"$ "+Color.End).strip()
            if len(plaintext) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            keyfile = input("├─[Enter the key file]"+color_banner[1]+"$ "+Color.End).strip()
            if len(keyfile) == 0:
                slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                again()
            outputfile = input("├─[Enter the output file]"+color_banner[1]+"$ "+Color.End).strip()
            if len(outputfile) == 0:
                slowprint("└─["+Color.BRed+"output file be empty"+Color.End+"]")
                again()
            public, private = readKeysFromFile(keyfile)
            publickey_encrypt(plaintext,public,outputfile)
            print(f"└─[The ciphertext was saved in file {outputfile}]")
            again()

        #::::: Decryption :::::
        elif(pick == "2" or pick == "02"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            encrypted_file = input("\n┌───(christopher)─[Public Key Cipher/Decryption]\n├─[Enter your Encrypted file]"+color_banner[1]+"$ "+Color.End).strip()
            if len(encrypted_file) == 0:
                slowprint("└─["+Color.BRed+"Plaintext cannot be empty"+Color.End+"]")
                again()
            keyfile = input("├─[Enter the key file]"+color_banner[1]+"$ "+Color.End).strip()
            if len(keyfile) == 0:
                slowprint("└─["+Color.BRed+"key cannot be empty"+Color.End+"]")
                again()
            public, private = readKeysFromFile(keyfile)
            print(f"└─[Plaintext: {publickey_decrypt(encrypted_file, private)}]")
            again()

        #::::: Key Generator :::::
        elif(pick == "3" or pick == "03"):
            clearScr()
            time.sleep(0.4)
            print(Banner.banner)
            try:
                keysize = int(input("\n┌───(christopher)─[Public Key Cipher/Key Generator]\n├─[Enter the key size]"+color_banner[1]+"$ "+Color.End))
                if keysize <= 1:
                    slowprint("└─["+Color.BRed+"The key size value must be greater than 1"+Color.End+"]")
                    again()
                filename = input("├─[Enter the name of the file]"+color_banner[1]+"$ "+Color.End).strip()
                if len(filename) == 0:
                    slowprint("└─["+Color.BRed+"File name cannot be empty"+Color.End+"]")
                    again()
                publickey, privatekey = generateKeys(keysize)
                writeKeysToFile(keysize, publickey, privatekey, filename)
                print(f"└─[Public key and Private key saved on {filename}_Public.key and {filename}_Private.key]")
                again()
            except ValueError:
                slowprint("└─["+Color.BRed+"Key Size value must be a number"+Color.End+"]")
                again()

        #::::: Back to Main Menu :::::
        elif (pick == "99"):
            christopher()
        else:
            again()

    #::::: Exit :::::
    elif (choice == "99"):
        print("\n\tGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()

    else:
        again()

try:
    christopher()
    again()
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()
    sys.exit()