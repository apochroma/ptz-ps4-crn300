import msgpack
from urllib.request import urlopen

#print("Hello World");

data_loaded = msgpack.unpack(urlopen('http://10.10.10.100/-wvhttp-01-/meta.cgi'))

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

if posX < 5000:
	posV = round(((posX + width / 2) / 5000) * -100)
else:
	posV = round(((posX / 5000) - 1) * 100)

print("posV: ",posV)

ip = "10.10.10.100"
url = "http://" + str(ip) + "/-wvhttp-01-/control.cgi?pan=v" + str(posV)
print(url)
command = urlopen(url).read()



#http://10.10.10.100/-wvhttp-01-/control.cgi?pan=left&pan.speed=500



#url = "http://10.10.10.100/-wvhttp-01-/control.cgi?pan=left"
#urlopen(url).read()

#http://10.10.10.100/-wvhttp-01-/control.cgi?pan=left

#data_loaded: {'version': '01.00', 'timestamp': '20561.490', 'realtime': '1659709548.088', 'detect': [{'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}], 'fguide': [{'status': False, 'level': 0, 'angle': 0, 'dir': 'behind', 'pos': {'x': 0, 'y': 0, 'w': 1, 'h': 1}}]}
#detect:  {'type': 'face', 'pos': {'x': 8288, 'y': 4310, 'w': 1099, 'h': 1953}, 'main': True, 'track': False}