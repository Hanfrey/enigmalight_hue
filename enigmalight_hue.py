#!/usr/bin/env python
import sys
import os
import time 
import json
import httplib
from rgb_xy import Converter
from rgb_xy import GamutC # or GamutB, GamutC
counter = 0

			
def popen():
	converter = Converter(GamutC)
	spidev = file( os.getcwd()+'/aufruf.log', "wb")
	key = "PmjwE4N6FkA6mFA6hgS6b5Wi2oeOeLPrNRGWcy72"
	ip = "192.168.1.X"
	url = '/api/' + key + '/lights/'
	lurl = url + '2/state'
	rurl = url + '1/state'
	burl = url + '4/state'
	#need to be sure that its not 0
	MINIMAL_VALUE=0.000000001

	while True:
		eingabe = sys.stdin.readline()

		if len(eingabe)>0:
			global counter
			counter+= 1
			# Get Input
			try:
				lr,lg,lb,rr,rg,rb,br,bg,bb,x = eingabe.split(' ')
			except ValueError:
				spidev.write("Not enough input parameter, do you have the same amount of lights (channels) in your enigmalight config?")
				spidev.flush()
				raise

			lr = (float(lr)+MINIMAL_VALUE)*255
			lg = (float(lg)+MINIMAL_VALUE)*255
			lb = (float(lb)+MINIMAL_VALUE)*255 
			rr = (float(rr)+MINIMAL_VALUE)*255
			rg = (float(rg)+MINIMAL_VALUE)*255
			rb = (float(rb)+MINIMAL_VALUE)*255
			br = (float(br)+MINIMAL_VALUE)*255
			bg = (float(bg)+MINIMAL_VALUE)*255
			bb = (float(bb)+MINIMAL_VALUE)*255

			lon = True
			ron = True
			bon = True
			
			if (lr + lg + lb < 10):
				lll = 1
				lon = False
			else:
				lll = (lr + lg + lb)
			
			if (rr + rg + rb < 10):
				llr = 1
				ron = False
			else:
				llr = (rr + rg + rb)

			if (br + bg + bb < 10):
				llb = 1
				bon = False
			else:
				llb = (br + bg + bb)
				
			if (lll >=255):
				lll = 254
				
			if (lll<1):
				lll = 1

			if (llr >=255):
				llr = 254
				
			if (llr<1):
				lllr = 1

			if (llb >=255):
				llb = 254
				
			if (llb<1):
				llb = 1

			lparams = {'xy': converter.rgb_to_xy(lr,lg,lb), 'colormode': 'xy', 'bri': int(lll), 'on': lon}
			rparams = {'xy': converter.rgb_to_xy(rr,rg,rb), 'colormode': 'xy', 'bri': int(llr), 'on': ron}
			bparams = {'xy': converter.rgb_to_xy(br,bg,bb), 'colormode': 'xy', 'bri': int(llb), 'on': bon}
			
			if (counter>=10):
				connection = httplib.HTTPConnection(ip, timeout=10)
			
				#connection.request('PUT', lurl, json.dumps(lparams))
				#response = connection.getresponse()
			
				#connection.request('PUT', rurl, json.dumps(rparams))
				#response = connection.getresponse()

				connection.request('PUT', burl, json.dumps(bparams))
				response = connection.getresponse()

				#data = response.read()

				connection.close()
				counter=0
		else:
			break
			
import time
time.sleep(7)
popen()