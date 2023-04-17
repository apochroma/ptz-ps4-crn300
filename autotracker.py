import time
import msgpack
from urllib.request import urlopen

#Activate Face detection and tracking
urlopen('http://10.10.10.100/-wvhttp-01-/control.cgi?c.1.focus.detect=facecatch').read()

face = posX = width = 0
while True:
	
	ramp=1
	deadband = 500
	absoluteM = 5000
	tracking = False
	data_loaded = msgpack.unpack(urlopen('http://10.10.10.100/-wvhttp-01-/meta.cgi'))
	
	for detect in data_loaded["detect"]:
		tracking = detect['track']
		print("everything: ", detect)
		print("Tracking detected: ", tracking)

		#if tracking == True:
		#	print("Face NOT detected")
		#	continue
		#else:
		print("Face detected")
		#print everything
		print("detect: ",detect)
		#print("Position: ",detect['pos']['x'])
		#set variable posX
		face = detect['type']
		posX = detect['pos']['x']
		width = detect['pos']['w']
		print("face: ", face)
		print("posX: ", posX)
		print("width: ", width)
	
	def getV(posX, width, absoluteM):
		if tracking == True:
			faceM = posX
			# faceM value between 1 and <10000
			if faceM >= absoluteM + deadband:
				#v=(faceM - absoluteM) / 10000 #we need an integer as percentage from 1..100
				#double the percentage to move subject to the midpoint
				v=((faceM - absoluteM) / 10000)*200
			elif faceM < absoluteM - deadband:
				v=((absoluteM - faceM) / 10000)*-200
			else:
				#this case can't be
				v=0
			url = 'http://10.10.10.100/-wvhttp-01-/control.cgi?pan.ramp=' + str(ramp) + '&pan=v' + str(int(v))
			print(url)
			command = urlopen(url).read()
		else:
			print("nothing to do because can't track")
			v=0
			url = 'http://10.10.10.100/-wvhttp-01-/control.cgi?pan.ramp=' + str(ramp) + '&pan=v' + str(int(v))
			print(url)
			command = urlopen(url).read()
	
	aufruf=getV(posX, width, absoluteM)
	time.sleep(1)

#data_loaded: {'version': '01.00', 'timestamp': '20561.490', 'realtime': '1659709548.088', 'detect': [{'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}], 'fguide': [{'status': False, 'level': 0, 'angle': 0, 'dir': 'behind', 'pos': {'x': 0, 'y': 0, 'w': 1, 'h': 1}}]}
#detect:  {'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}