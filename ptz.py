#!/usr/bin/env python3

import sys
import time

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen


# Your code where you can use urlopen
# with urlopen("http://www.python.org") as url:
#    s = url.read()

#print(s)


from pyPS4Controller.controller import Controller

ip = "10.10.10.100"
speed_list = [10, 40, 75, 300, 600, 1250, 2500, 5000, 7500, 10000]
i = 4
speed = 0

def inc_speed(*args):
	#read speed
	#enumerate index of speed
	#do calc do count
	global i
	global speed
	if i < len(speed_list)-1: # i <= 7
		#print(len(speed_list))
		i += 1
		print("You increased speed")
	elif i >= len(speed_list)-1: # i >= 7
		print("You are as fast as possible!")

	speed = speed_list[i]
	#print("inside inc_speed() speed is: " + str(speed))
	return (speed, i)

def dec_speed(*args):
	#read speed
	#enumerate index of speed
	#do calc do count
	global i
	global speed
	if i > 0:
		i -= 1
		print("You decreased speed")
	elif i <= 0:
		print("You are as slow as possible!")

	speed = speed_list[i]
	#print("inside inc_speed() speed is: " + str(speed))
	return (speed, i)

def info_ptz(arg1):
	ip = "10.10.10.100"
	url = "http://" + str(ip) + "/-wvhttp-01-/info.cgi?itme=" + str(arg1)
	response = urlopen(url).read()
	print(response)

def control_ptz(arg1, arg2):
	ip = "10.10.10.100"
	arg2 = "&pan.speed=" + str(speed) + "&tilt.speed=" + str(speed)
	url = "http://" + str(ip) + "/-wvhttp-01-/control.cgi?" + str(arg1) + str(arg2)
	print(url)
	command = urlopen(url).read()



	#print("Speedlist is: " + str(speed_list()))
	#print("Speed Index 0 is: " + str(speed_list([0])))
	
class MyController(Controller):

	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)
		self.last_value = 0

	def on_R3_up(self, value):
		
		if self.last_value == value:
			return
		self.last_value = value
		
		speed_index = value / (32767 / (len(speed_list)-2))*-1
		print("value: " +str(value)+ " speed index: " +str(speed_index))
		#print(speed)
		pt_speed = speed_list[speed_index]
		direction = "&tilt=up"
		pt_speed = "&tilt.speed=" + str(pt_speed)

		url = "http://" + str(ip) + "/-wvhttp-01-/control.cgi?" + direction + pt_speed
		print(url)
		command = urlopen(url).read()

	def on_right_arrow_press(self):
		inc_speed(i)
		#print(i)
		#print(speed)
		#print(str(i) + " multiplied with " + str(speed) + " results in " + str(speed*i))

	def on_left_arrow_press(self):
		dec_speed(i)
		print(i)
		print(speed)
		print(str(i) + " multiplied with " + str(speed) + " results in " + str(speed*i))

	def on_x_press(self):
		arg1 = "tilt=down&tilt.speed.mode.list=auto2" 
		arg2 = ""
		control_ptz(arg1, arg2)
		getinfo = "c.1.pan.speed.dir"
		info_ptz(getinfo)
		print("Move PTZ camera down")

	def on_x_press(self):
		arg1 = "tilt=down&tilt.speed.mode.list=auto2" 
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Move PTZ camera down")

	def on_x_release(self):
		arg1 = "tilt=stop" 
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Stop PTZ camera")

	def on_triangle_press(self):
		arg1 = "tilt=up&tilt.speed.mode.list=auto2"
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Move PTZ camera down")

	def on_triangle_release(self):
		arg1 = "tilt=stop"
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Stop PTZ camera")

	def on_square_press(self):
		arg1 = "pan=left&pan.speed.mode.list=auto2"
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Move PTZ camera left")

	def on_L3_left(self):
		arg1 = "pan=left&pan.speed.mode.list=auto2" 
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Move PTZ camera left")
	
	def on_square_release(self):
		arg1 = "pan=stop" 
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Stop PTZ camera")

	def on_circle_press(self):
		arg1 = "pan=right&pan.speed.mode.list=auto2" 
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Move PTZ camera right")

	def on_circle_release(self):
		arg1 = "pan=stop"
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Stop PTZ camera")

	
	def on_L2_press(self, value):
		arg1 = "zoom=tele" 
		arg2 = "" 
		control_ptz(arg1, arg2)
		print("Zoom In")

	def on_L2_release(self):
		arg1 = "zoom=stop"
		arg2 = "" 
		control_ptz(arg1, arg2)
		print("Zoom Stop")

	"""
	def on_L2_press(self, value):
		global speed
		speed = 0
		value = int((value + 32767) / 2184.46) # result 1-30
		if value == 30: speed = 9900
		if value == 29: speed = 7000
		if value == 28: speed = 5000
		if value == 27: speed = 3000
		if value == 26: speed = 2000
		if value == 25: speed = 1000
		if value == 24: speed = 750
		if value == 23: speed = 500
		if value == 22: speed = 400
		if value == 21: speed = 300
		if value == 20: speed = 250
		if value == 19: speed = 200
		if value == 18: speed = 150
		if value == 17: speed = 100
		if value == 16: speed = 90
		if value == 15: speed = 80
		if value == 14: speed = 70
		if value == 13: speed = 60
		if value == 12: speed = 50
		if value == 11: speed = 45
		if value == 10: speed = 40
		if value == 9: speed = 35
		if value == 8: speed = 30
		if value == 7: speed = 25
		if value == 6: speed = 22
		if value == 5: speed = 20
		if value == 4: speed = 17
		if value == 3: speed = 15
		if value == 2: speed = 12
		if value == 1: speed = 10
		arg1 = "" 
		arg2 = "pan=right&pan.speed=" + str(speed)
		#print("Value: " + str(value))
		#print("Speed: " + str(speed))
		#arg1 = "&pan.speed=" + str(speed)
		time.sleep(0.05)
		control_ptz(arg1, arg2)


	def on_L2_release(self):
		arg1 = "zoom=stop"
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Zoom Stop")
	"""

	def on_R2_press(self, value):
		arg1 = "zoom=wide"
		arg2 = "&zoom.speed=" +str(i)
		control_ptz(arg1, arg2)
		print("Zoom In")

	def on_R2_release(self):
		arg1 = "zoom=stop"
		arg2 = ""
		control_ptz(arg1, arg2)
		print("Zoom Stop")

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60*60*3)
