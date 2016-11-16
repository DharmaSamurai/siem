#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, Response, request 

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_data():
	if request.method == 'POST':
		print('Recieved from client: ', request.data)
	return Response('OK')

if __name__ == '__main__':
	app.run(debug=True)