#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from hashlib import sha256
from hmac import HMAC
import os


def encrypt_password(password,salt = None):
    if salt is None:
        salt = os.urandom(8)

    if isinstance(salt,str):
        salt = salt.encode('utf-8')

    new_password = password.encode('utf-8')
    encrypt_password = HMAC(salt,new_password,sha256).hexdigest()
    print("Encrypt passwrod is %s."% encrypt_password )

if __name__ == '__main__':
    raw_password = input("Please input your password:")
    encrypt_password(raw_password)
