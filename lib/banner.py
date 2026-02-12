import os
#::::: Library :::::
from lib.color import Color, color_banner

#::::: Banner :::::
class Banner:
    "A Class to print different banner."

    #::::: Main Menu :::::
    cipher_banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/
    [01]Atbash Cipher        [02]Caesar Cipher
    [03]Affine Cipher        [04]Vigenère Cipher
    [05]Reverse Text         [06]Playfire Cipher
    [07]Rail Fence Cipher    [08]Scytale Cipher
    [09]Polybius Square      [10]Columnar Cipher
    [11]Substitution Cipher  [12]Baconian Cipher
    [13]Morse Code           [14]Rot13 Cipher
    [15]One-Time Pad Cipher  [16]Hash Function
    [17]Enigma Machine       [18]Public Key Cipher""")

    #::::: Main Menu (Empty) :::::
    banner = (Color.End + r"""
\ \ """+color_banner[0]+r"""Pp  Uu  Ee  Vv  Ff  Gg  Bb  Cc  Uu  Rr  Ee"""+Color.End+r""" / /
 \ \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ /
  \ """+color_banner[1]+r"""        abcdefghijklm-nopqrstuvwxyz        """+Color.End+r"""/
   \__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/
   /"""+color_banner[2]+r"""Cc  Hh  Rr  Ii  Ss  Tt  Oo  Pp  Hh  Ee  Rr"""+Color.End+r"""\
   \__________________________________________/""")

    #:::: Github ::::
    github_banner = (color_banner[0]+r"""╔══════════════════════════════════════════╗
║   """+Color.End+r"""["""+color_banner[1]+r"""+"""+Color.End+r"""]Christopher"""+color_banner[0]+r"""                         ║
║   """+Color.End+r"""["""+color_banner[2]+r"""+"""+Color.End+r"""]Tool for Encryption & Decryption"""+color_banner[1]+r"""    ║
║   """+Color.End+r"""["""+color_banner[3]+r"""+"""+Color.End+r"""]Version: 1.0"""+color_banner[0]+r"""                        ║
╚══════════════════════════════════════════╝"""+Color.End)