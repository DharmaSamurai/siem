#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import uuid

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import rsa

from base64 import b64decode

sec_key = b'-----BEGIN PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,D6D1B2C84B504120\n\nyXgGDMvaMafUdMT+tYor/J8Ps9Fc7deAmfPvR0OhWE4TXWbn2lR+PLtQ7jDVLpTI\n+aoMEmWaO+WSInovzeCgs2kmcvPuiQfYxxUemsWZxfsvl301nQHxfeJGmo+BfXmB\ngu1hbEzheAtDBzxZonmcZPrXxMwxwNCqJMgy2JerBQszUeTwvcvNGprfGMOsYXEW\nTlWFe9FGzBC/udBwAIGLRI3huSd/oivK22Oao8bwtsYqijyOX6p2CDYsnVOAh1Ty\n/rBj5UmBbuyWvkpSjP0WQAcjVutyas15Lapi7iDFveA1Fgn06qpXLw8Ofo1Rrkhp\nZskMusIied4IitNmsuiVt4yM1Jx6OcN5Xc0qr7e0JO055k4BH5q+TqbHWdZOadUw\n8XPh1xNQnuHpJ6hsCpLiefh2eSHEfJ2Eeaj9FU7bNoJYzDsM50oMH4qNcaKYUfaD\no57WC7nqcBSc58KB/FqwEKU4Cja9oTZE3Dx0MQhjlrgPJHga+L0rKZuZBsYzcWDB\n6oRfaRhujz5UY9wio6yfKaB1rnnz+UR/D1e96GYWa+MYAresEkwzVNtQRHCr8sX4\nVLG7kJIKZAANp+n5E3AydWebQ5uiz1mQl3//cNknTmrPhXsbV7166d8P0POQmmuF\nEpCnq7BIzna26zJnqIXgvqAWomtwtrPqU4fPgEzY80jRKjhtX9oVv4buBM50GoBj\nnGzgoGPog05Lx1UZnuzwjSll59D/fvP8QZC5qFOG2mo/dTcSfALR6/3UD1N1UtH6\n9snyKsXsv9uy2eRMCTxfyLMDgAzl/5sc1FzAi+0dl/259XXW7yd+DGidj+3oVjun\nitnkEmVHATy3Gq6oKgzjpsAiAo4OJDameoIB7HOG/+geB2lmUVGtL58Wh37efVJn\n44k+i6fbgi9WCEI0LxqUPmUCCkDFUETtRhghUcr8lWsPRv3MchZ7m0zw34Yrkny8\nGIl/bU2UYHu/neINOvbewyOh1xTm12oq5KKj6rIjyO/rn8ms4FQA7/pmh7dzQuWB\ng8xD3W4D9wVZTSYk0J5LM0tahsIJlc0p3oOJP1ZFqIbwmaDVM4lEtIjKN0dNRf4L\nDZNcpXDpoXGc0zD6RAGLeIiDU0isjxUlACv7dmBW+9jsnxKLBi/aWMEN+VSs+mmZ\nUalH1hZ6j3JU9ZtTPJTvHuQG43hIhA41f4e0dEDdyxc9zHhHfKv9bwZBCYVTOvdU\nVT6Vp309jr+ox6OSMfr3bPwPmc9kS5SXBTkx/+4/W+tgjZ4YfU53wD3h+D8cBKdm\nY5i3umT992wfARO23My2Pwp8BNeH2Nd3++ktM2QjtoLRBexqqrtnRnkg4JvfrMv7\nBGmKgPPIIeyTmGiu7Go/XByUMp3jrHSNu8jRRq06ZINMZ8PpakfT+YcdMd2XBpmi\n1aK43HiXTuW0LRZIMaSjPpEpyFuX7AyH9Lx3IdDBvceXXfppQ4U+3f038U0U+rx4\nsRK9yTsYaunuf47I0dLkKEwBMBv3DsPvzvsG0iWlDE0SPQ6BaUUv12JAeERoEsPt\n+N69IE2Cqc/uZk5wax6y4UB/ZhNLL6Rv0DjgGeW/4Rnd3aA2yVWO3K6tG/sOvBP4\n6r5pN+C10ZahBPcOhbpxttkpygwTW0Jx\n-----END PRIVATE KEY-----'
pub_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7DQBShLA3mUEW3IGVGQ6\nwQhTdrFqK+/v4oFx77GesJf0lO4tyw8HMANO7zq9JEExhWiIaSwV1AccsQ4AKG/b\n9192H5jU7qe3PIAOyfIRYS+BMyUoAfR4yWPMDJ+4dmdvv6wBLAt/EBxEZRCbrJJR\n4TzqyfceXLK+DMZueITxqlfTAy3z9I4JkmqRl439HvKoGMRN2T8QjsCq83FIVqDN\ncJ8AcKOQ/l+HtDueI45BKptrKvs0rQYk7/RibRZUE5rBvGD/DryDdgDqANcsfpC7\n/ZtxB/TS06udMA9PgnS0IXSO5/CnJ/Kw+RiHdg7z8IEWqo4OKzas2zlYr/31aof3\nTQIDAQAB\n-----END PUBLIC KEY-----'


def rand_num():
	''' создает 128-битное число '''
	number = str(uuid.uuid4().int)
	number = number.encode('utf-8')
	return number


def crypt_rsa(data, key):
	''' шифрует RSA данные data ключем key '''
	key = RSA.importKey(key)
	cipher = PKCS1_OAEP.new(key)
	return cipher.encrypt(data)


# TEST
data = rand_num()
encrptd = crypt_rsa(data, pub_key)

# УДАЛИТЬ ЭТУ СТРОКУ ПРОСТО ФИКСА ПЕРЕДАЧИ ИНФЫ МЕЖДУ КЛИЕНТОМ И СЕРВЕРОМ
data = b'22778011885280259212060222157222796759'

# Sending message
r = requests.post("http://127.0.0.1:5000", data=data)
answr = r.content

print('Data sent: ', data)
print('Encrypted with RSA: ', encrptd)
print('Answer: ', answr)


def decrypt_rsa(data, key):
	''' дешифрует RSA данные data ключем key '''
	key = key.decode()
	key = key.replace('\n-----END PRIVATE KEY-----', '').replace('-----BEGIN PRIVATE KEY-----\n', '')
	key = key.encode()
	print('KEY IS HERE: ', key)

	key = b64decode(key)

	print('KEY 2 IS HERE: ', key)

	key = RSA.importKey(key)
	
	cipher = PKCS1_OAEP.new(key)
	decrypted = cipher.decrypt(data)
	return decrypted


decrptd = decrypt_rsa(answr, sec_key)
print('Decrypted with RSA: ', decrptd)


# Проверяем совпадают ли данные
if data == decrptd:
	print("CORRECT !!! YES !!! WE DID IT !!!")
else:
	print("NOT CORRECT !!!")


# PUBKEY_TEMPLATE = "-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----"

# def generate_keys():
# 	''' генерирует RSA ключи '''
# 	secret_code = "Unguessable"
# 	key = RSA.generate(2048)
# 	encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8)
# 	public_key = key.publickey().exportKey()
# 	keys = [encrypted_key, public_key]
# 	return keys
