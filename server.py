#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, Response, request 
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

app = Flask(__name__)

# RSA keys
sec_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAtPOtcrcUylmKB5PTB6xQYpEU0Gder9m/dukfRBMhNNdyjUCS\n9k/wKsbOA0YfaT0ZGFBR+lGJWtX9p18HuZwEdhssFcC2T1JeB7CzCU1g1IRBQxKH\noEfzy/pNI3d5PHGCMf+WifwCYDOkERoUAFD5ORyKfcRG2kap8Y8zxOa1OwVLVAKw\nIDcclICBTvsUPO5ICA0c5IyQRjBgvk26Jjp/A+ZNZkS6VAoo+i0oEPVoMJ4FxdZk\nQ1w00luYyL2AxKhRNV3lSJqf7ysUWbUF0O2nOnyqTEkLrTXGGy5dgS5dFWbKD+81\n749Y25pYwBCb4DuNhrinvNg1BizZbBcL/f+hgwIDAQABAoIBAD1HcGuy2JWWMQpT\n41lr32Uh4Lya5RQEV7S7Sd1R5SLx+1cekSZc9+ZkoQu2yZhoGoGDYd+1kSBz64ys\nv/75eQFOPmW3d4XxTOqpylfSHoKZr0g5lDiRZVykjU7/fM0dW4v3FFHySBOwKVWp\nUTCyO1Q9+CCTQbNVzuOBLXT29FTh6lOGb1LFJm9tB15NuO4AJO7RWgTQ7EC/dU+D\n44lwlEvJ4XqXUR/u/3K6j0dkmjHfQwB28hph+eU7h4l44/14ep9bPSn60adY2LJE\n7jvxxMgfwlBXS3sOlf+ikkRqdFupZ1wHrg09OhL3Iuc3Lh00noSokqvuCtefS2IC\nRczFvJECgYEA1jqUKyMhzgzNWPxHV1LJkjlZIIQ6nR96NEYDWKsLN3VtVi1E50Mx\n7I/u26jPJNggnNN8C/sdddHYHIukYQZoEDgNR6t42NEMmK3xqH53QIon0fRS2nAa\nF/g4BSJvMT4iOemFgOSWb1El+QsDHwiDugf0f+9YpapIk1duQrZarj8CgYEA2DwM\nycRxUPgB4kTwsiT7FRh5tAGEe3i0BxA2C2rZrCJp9L+xF50DJurmlsJ9fiq6BqbN\nM0lrtHftS5jW/ZLIdDSLXf9oSCRvLdKANDnBWEt3Wgm8+4eBfvUSJRNe/IZATnpx\nP/qIP+7iZJIf82oVlT1OWSpMPrZp/rBzRIbtw70CgYEAgPmDevULxSGv/4Li8I/H\nC2G7Zvg00aPBzvbXzOotNpZb3SYj9Zde1y1QgK6BB42XFNO+OvhUJDrSAV2Q+VkC\nDcGxPRTfDKnPC5ytgOOiqBiFIMIXn6seCpBGKdExYFQoBvWwiokUiLAyTF1045oc\ntENV0DApDpQWXZ6lo0RmE8ECgYB5oU2QMO+Mm/RzUlQR4LtbImlS14et7DdXwcak\npXXLXZA8G5eBsNAVFAygwMXWMjJxi2Hhd2seGFdiLpbAC9C1jNjYBtKhwdzH6aAz\nwEkBYXHBM7kZwx8USsXqFPtZECsb+cO6OTJqw/SUnZ1bTlDVoaZwgVph7DmzCY3M\n/hjAAQKBgHlRoitEhp70lFtF6eKnbaSvlO5ldO9yOWDcokmfWbK65VA03XzT2BJF\nRrO0aTxofm2OTYNilfb9z5FiOdLi0RJEEiCW63oSgecybuoIj6Oy5i1f13kgLHrg\nrB1SUpAzD34DO30nJ0hSeI8QXxvVxY4D2hOao+3kEOELr0mP8apx\n-----END RSA PRIVATE KEY-----'
pub_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtPOtcrcUylmKB5PTB6xQ\nYpEU0Gder9m/dukfRBMhNNdyjUCS9k/wKsbOA0YfaT0ZGFBR+lGJWtX9p18HuZwE\ndhssFcC2T1JeB7CzCU1g1IRBQxKHoEfzy/pNI3d5PHGCMf+WifwCYDOkERoUAFD5\nORyKfcRG2kap8Y8zxOa1OwVLVAKwIDcclICBTvsUPO5ICA0c5IyQRjBgvk26Jjp/\nA+ZNZkS6VAoo+i0oEPVoMJ4FxdZkQ1w00luYyL2AxKhRNV3lSJqf7ysUWbUF0O2n\nOnyqTEkLrTXGGy5dgS5dFWbKD+81749Y25pYwBCb4DuNhrinvNg1BizZbBcL/f+h\ngwIDAQAB\n-----END PUBLIC KEY-----'

# AES keys
aes_key = b'Sixteen byte key'
aes_data = b'Attack at dawn'


@app.route('/', methods=['POST', 'GET'])
def start():
	if request.method == 'POST':
		dt = request.data
		dt = base64.b64decode(dt)

		# Если получили число, шифруем его и отправляем обратно
		if dt.isdigit():
			print('Recieved RSA from client: ', dt)
			encrptd = crypt_rsa(dt, pub_key)
			return Response(encrptd)
		# Усли получили AES, расшифровываем его
		else:
			print('Recieved AES from client: ', dt)
			dt = base64.b64encode(dt)
			decrypted = decrypt_aes(dt, aes_key)
			print('Decrypted: ', decrypted)
	return Response('Get Request')


def crypt_rsa(data, key):
	''' шифрует RSA данные data ключем key '''
	key = RSA.importKey(key)
	cipher = PKCS1_OAEP.new(key)
	return cipher.encrypt(data)


def decrypt_aes(data, key):
	''' расшифровываем AES данные data ключем key '''
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CFB, iv)
	return cipher.decrypt(base64.b64decode(data))


if __name__ == '__main__':
	app.run(debug=True)