from pyPS4Controller.controller import Controller

speed_list = (10, 25, 75, 300, 600, 1250, 2500, 5000, 7500, 10000) # this is a tuple

speed = on_L1_press(print())

class MyController(Controller):

   def __init__(self, **kwargs):
      Controller.__init__(self, **kwargs) 
   def on_x_press(self):
      print("Hello world")    
   def on_x_release(self):
      print("Goodbye world")
   def on_L1_press(self, value):
      self.speed = value


class PTZ(self, speed=None, zoom=None, direction=None)
   def __init__(self):
      self.speed = speed
      self.zoom = zoom
      self.direction = direction


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60*60*3) # 3 hours