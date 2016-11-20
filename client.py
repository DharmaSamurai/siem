#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import uuid

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random
from Crypto.PublicKey import RSA


sec_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAtPOtcrcUylmKB5PTB6xQYpEU0Gder9m/dukfRBMhNNdyjUCS\n9k/wKsbOA0YfaT0ZGFBR+lGJWtX9p18HuZwEdhssFcC2T1JeB7CzCU1g1IRBQxKH\noEfzy/pNI3d5PHGCMf+WifwCYDOkERoUAFD5ORyKfcRG2kap8Y8zxOa1OwVLVAKw\nIDcclICBTvsUPO5ICA0c5IyQRjBgvk26Jjp/A+ZNZkS6VAoo+i0oEPVoMJ4FxdZk\nQ1w00luYyL2AxKhRNV3lSJqf7ysUWbUF0O2nOnyqTEkLrTXGGy5dgS5dFWbKD+81\n749Y25pYwBCb4DuNhrinvNg1BizZbBcL/f+hgwIDAQABAoIBAD1HcGuy2JWWMQpT\n41lr32Uh4Lya5RQEV7S7Sd1R5SLx+1cekSZc9+ZkoQu2yZhoGoGDYd+1kSBz64ys\nv/75eQFOPmW3d4XxTOqpylfSHoKZr0g5lDiRZVykjU7/fM0dW4v3FFHySBOwKVWp\nUTCyO1Q9+CCTQbNVzuOBLXT29FTh6lOGb1LFJm9tB15NuO4AJO7RWgTQ7EC/dU+D\n44lwlEvJ4XqXUR/u/3K6j0dkmjHfQwB28hph+eU7h4l44/14ep9bPSn60adY2LJE\n7jvxxMgfwlBXS3sOlf+ikkRqdFupZ1wHrg09OhL3Iuc3Lh00noSokqvuCtefS2IC\nRczFvJECgYEA1jqUKyMhzgzNWPxHV1LJkjlZIIQ6nR96NEYDWKsLN3VtVi1E50Mx\n7I/u26jPJNggnNN8C/sdddHYHIukYQZoEDgNR6t42NEMmK3xqH53QIon0fRS2nAa\nF/g4BSJvMT4iOemFgOSWb1El+QsDHwiDugf0f+9YpapIk1duQrZarj8CgYEA2DwM\nycRxUPgB4kTwsiT7FRh5tAGEe3i0BxA2C2rZrCJp9L+xF50DJurmlsJ9fiq6BqbN\nM0lrtHftS5jW/ZLIdDSLXf9oSCRvLdKANDnBWEt3Wgm8+4eBfvUSJRNe/IZATnpx\nP/qIP+7iZJIf82oVlT1OWSpMPrZp/rBzRIbtw70CgYEAgPmDevULxSGv/4Li8I/H\nC2G7Zvg00aPBzvbXzOotNpZb3SYj9Zde1y1QgK6BB42XFNO+OvhUJDrSAV2Q+VkC\nDcGxPRTfDKnPC5ytgOOiqBiFIMIXn6seCpBGKdExYFQoBvWwiokUiLAyTF1045oc\ntENV0DApDpQWXZ6lo0RmE8ECgYB5oU2QMO+Mm/RzUlQR4LtbImlS14et7DdXwcak\npXXLXZA8G5eBsNAVFAygwMXWMjJxi2Hhd2seGFdiLpbAC9C1jNjYBtKhwdzH6aAz\nwEkBYXHBM7kZwx8USsXqFPtZECsb+cO6OTJqw/SUnZ1bTlDVoaZwgVph7DmzCY3M\n/hjAAQKBgHlRoitEhp70lFtF6eKnbaSvlO5ldO9yOWDcokmfWbK65VA03XzT2BJF\nRrO0aTxofm2OTYNilfb9z5FiOdLi0RJEEiCW63oSgecybuoIj6Oy5i1f13kgLHrg\nrB1SUpAzD34DO30nJ0hSeI8QXxvVxY4D2hOao+3kEOELr0mP8apx\n-----END RSA PRIVATE KEY-----'
pub_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtPOtcrcUylmKB5PTB6xQ\nYpEU0Gder9m/dukfRBMhNNdyjUCS9k/wKsbOA0YfaT0ZGFBR+lGJWtX9p18HuZwE\ndhssFcC2T1JeB7CzCU1g1IRBQxKHoEfzy/pNI3d5PHGCMf+WifwCYDOkERoUAFD5\nORyKfcRG2kap8Y8zxOa1OwVLVAKwIDcclICBTvsUPO5ICA0c5IyQRjBgvk26Jjp/\nA+ZNZkS6VAoo+i0oEPVoMJ4FxdZkQ1w00luYyL2AxKhRNV3lSJqf7ysUWbUF0O2n\nOnyqTEkLrTXGGy5dgS5dFWbKD+81749Y25pYwBCb4DuNhrinvNg1BizZbBcL/f+h\ngwIDAQAB\n-----END PUBLIC KEY-----'


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

# Суть проблемы:
# http://python.su/forum/topic/31377/?page=1#post-170659
# УДАЛИТЬ ЭТУ СТРОКУ ПОСЛЕ ФИКСА ПЕРЕДАЧИ ИНФЫ МЕЖДУ КЛИЕНТОМ И СЕРВЕРОМ
data = b'22778011885280259212060222157222796759'

# Sending message
r = requests.post("http://127.0.0.1:5000", data=data)
answr = r.content


def decrypt_rsa(data, key):
	''' дешифрует RSA данные data ключем key '''
	key = RSA.importKey(key)
	cipher = PKCS1_OAEP.new(key)
	decrypted = cipher.decrypt(data)
	return decrypted


decrptd = decrypt_rsa(answr, sec_key)
print('Decrypted with RSA: ', decrptd)


# А теперь шифрование AES
def send_aes():
	key = b'Sixteen byte key'
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CFB, iv)
	msg = iv + cipher.encrypt(b'Attack at dawn')
	r = requests.post("http://127.0.0.1:5000", data=msg)
	print('Message encrypted by AES: ', msg)


# Проверяем совпадают ли данные
if data == decrptd:
	print("CORRECT !!! YES !!! WE DID IT !!!")
	send_aes()
else:
	print("NOT CORRECT !!!")



# PUBKEY_TEMPLATE = "-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----"

# def generate_keys():
# 	''' генерирует RSA ключи '''
# 	k = RSA.generate(2048)
# 	sk = k.exportKey() #PrivateKey
# 	pk = k.publickey().exportKey() #PublicKey
# 	return [sk, pk]
