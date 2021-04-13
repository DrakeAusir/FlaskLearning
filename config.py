import os

class Config(object):
	SECRET_KEY  = os.environ.get('SECRET_KEY') or b'\x9e\x8b\x16k\x95\xaa\xbf\xd7\xfc\xe4<\xa3\xb8u[\xa9'
	DEBUG = True
	TESTING = True
