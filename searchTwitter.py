#!/usr/bin/python3

# connect to tweeter, search for tweets containing a
# specific  stream and when 3 or more such tweets are 
# found, program print, “Ian G. Harris is popular!”

from twython import TwythonStreamer

exec(open("keys.py").read())

string = "Ian G. Harris" # searchs this string in stream tweets
nb = 0 # nb seen

def found():
	global nb
	nb = nb+1
	if ( nb > 2 ):
		print("Harris is popular!")

class TWStreamer(TwythonStreamer):

	def on_success(self, data):
		if 'text' in data:
			print("Found it.")
			found()
			print(data['text'].encode('utf-8'))

	def on_error(self, status_code, data):
		print(status_code)
		self.disconnect()

try:
	stream = TWStreamer(C_K, C_S, A_T, A_S)
	stream.statuses.filter(track = string)
except KeyboardInterrupt:
	exit()
