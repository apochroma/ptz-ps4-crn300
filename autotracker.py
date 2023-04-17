import time
import msgpack
from urllib.request import urlopen

while True:
	data_loaded = msgpack.unpack(urlopen('http://10.10.10.100/-wvhttp-01-/meta.cgi'))
	deadband = 400
	absoluteM = 5000
	
	for detect in data_loaded["detect"]:
		#print everything
		print("detect: ",detect)
		#print("Position: ",detect['pos']['x'])
		#set variable posX
		posX = detect['pos']['x']
		width = detect['pos']['w']
		print("posX: ", posX)
		print("width: ", width)
	
	def getV(posX, width, absoluteM):
		faceM = posX
		# faceM value between 1 and <10000
		if faceM >= absoluteM + deadband:
			#v=(faceM - absoluteM) / 10000 #we need an integer as percentage from 1..100
			#double the percentage to move subject to the midpoint
			v=((faceM - absoluteM) / 10000)*200
		elif faceM < absoluteM - deadband:
			v=((absoluteM - faceM) / 10000)*-200
		else:
			v=0
		url = 'http://10.10.10.100/-wvhttp-01-/control.cgi?pan.ramp=0&pan=v' + str(int(v))
		command = urlopen(url).read()
	
	aufruf=getV(posX, width, absoluteM)
	time.sleep(.5)

#data_loaded: {'version': '01.00', 'timestamp': '20561.490', 'realtime': '1659709548.088', 'detect': [{'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}], 'fguide': [{'status': False, 'level': 0, 'angle': 0, 'dir': 'behind', 'pos': {'x': 0, 'y': 0, 'w': 1, 'h': 1}}]}
#detect:  {'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}