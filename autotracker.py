import requests
import re
import time
import msgpack
from urllib.request import urlopen

#print("Hello World");


#while True:
data_loaded = msgpack.unpack(urlopen('http://10.10.10.100/-wvhttp-01-/meta.cgi'))

pan_all = urlopen('http://10.10.10.100/-wvhttp-01-/info.cgi?item=c.1.pan').read().decode('utf-8')

items=re.findall("^.*c.1.pan:=.*$",pan_all,re.MULTILINE)
for pan in items:
#	print (pan)
	pan = pan.replace('c.1.pan:=', '')
	print('pan: ', pan)

#exit()

#print(data == data_loaded)
#print("data:", data)
## print("data_loaded:", data_loaded)

posX = 0
width = 0

for detect in data_loaded["detect"]:
	#print everything
	print("detect: ",detect)
	#print("Position: ",detect['pos']['x'])
	#set variable posX
	posX = detect['pos']['x']
	width = detect['pos']['w']
	print("posX: ", posX)
	print("width: ", width)


#diese Kalkulation führt zu nichts
#posX = posX + (width / 2)
#if posX < 5000:
#	posV = round((posX / 5000) * -100)
#else:
#	posV = round(((posX / 5000) - 1) * 100)
#



faceM = posX + width / 2
absoluteM = 5000
distCam = 34000
if faceM <= 5000:
#	move cam left or negative value
#	Prozentualer Ausdruck von faceM bis Bildmitte zur gesamten Bildspannweite (10000):
	distFactor = (5000 - faceM) / 10000
	distToMove = distFactor * distCam
#	
#	http://10.10.10.100/-wvhttp-01-/info.cgi?item=c.1.pan:
#	Get absolute position of camera; subtract distToMove; move to new absolute position
	moveTo = int(pan) - distToMove
	url = 'http://10.10.10.100/-wvhttp-01-/control.cgi?pan.ramp=2&pan=' + str(moveTo)
	command = urlopen(url).read()


else:
#	move cam right or positive value
#	Prozentualer Ausdruck von faceM bis Bildmitte zur gesamten Bildspannweite (10000):
	distFactor = (faceM - 5000) / 10000
	distToMove = distFactor * distCam
#	
#	http://10.10.10.100/-wvhttp-01-/info.cgi?item=c.1.pan:
#	Get absolute position of camera; add distToMove; move to new absolute position
	moveTo = int(pan) + distToMove
	url = 'http://10.10.10.100/-wvhttp-01-/control.cgi?pan.ramp=2&pan=' + str(moveTo)
	command = urlopen(url).read()

#posX = posX + (width / 2)
#if posX < 5000:
#	posV = round((5000 - posX))
#else:
#	posV = round((posX - 5000))
#

#print("posV: ",posV)

#ip = "10.10.10.100"
##url = "http://" + str(ip) + "/-wvhttp-01-/control.cgi?pan.ramp=0&pan=v" + str(posV)
#url = "http://" + str(ip) + "/-wvhttp-01-/control.cgi?pan.ramp=0&pan=d" + str(posV)
#
#print(url)
#command = urlopen(url).read()
#time.sleep(1)



#http://10.10.10.100/-wvhttp-01-/control.cgi?pan=left&pan.speed=500



#url = "http://10.10.10.100/-wvhttp-01-/control.cgi?pan=left"
#urlopen(url).read()

#http://10.10.10.100/-wvhttp-01-/control.cgi?pan=left

#data_loaded: {'version': '01.00', 'timestamp': '20561.490', 'realtime': '1659709548.088', 'detect': [{'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}], 'fguide': [{'status': False, 'level': 0, 'angle': 0, 'dir': 'behind', 'pos': {'x': 0, 'y': 0, 'w': 1, 'h': 1}}]}
#detect:  {'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}