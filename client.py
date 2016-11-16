#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import uuid

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

# from base64 import b64decode


PUBKEY_TEMPLATE = "-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----"


def rand_num():
	''' создает 128-битное число '''
	number = str(uuid.uuid4().int)
	number = number.encode('utf-8')
	return number


def generate_keys():
	''' генерирует RSA ключи '''
	secret_code = "Unguessable"
	key = RSA.generate(2048)
	encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8)
	public_key = key.publickey().exportKey()
	keys = [encrypted_key, public_key]
	return keys


def crypt_rsa(data, key):
	''' шифрует RSA данные data ключем key '''
	key = RSA.importKey(key)
	cipher = PKCS1_OAEP.new(key)
	return cipher.encrypt(data)


# def decrypt_rsa(data, key):
# 	''' дешифрует RSA данные data ключем key '''
# 	key = RSA.importKey(key)
# 	cipher = PKCS1_OAEP.new(key)
# 	decrypted = cipher.decrypt(b64decode(data))
# 	return decrypted


# TEST
data = rand_num()
keys = generate_keys()
secret_key = keys[0]
pub_key = keys[1]

print('RANDOM NUM IS HERE: ', data)

encrptd = crypt_rsa(data, pub_key)
print('Encrypted with RSA: ', encrptd)

# decrptd = decrypt_rsa(encrptd, secret_key)
# print('Decrypted with RSA: ', decrptd)

# Sending message
r = requests.post("http://127.0.0.1:5000", data=data)
print('Data sent: ', data)