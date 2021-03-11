class Light:
    def __init__(self):
        self.state = False #indicates if light is on or off
        self.brightness  = 0 #indicates brightness level of a light from 0.01 to 1.0 (1.0 maps to max brightnes, and 0.01 maps to 1% of max brightness )
        self.powerMeter = 0 #attribute that count's power Consumption in kW/h
    def getPowerConsumption(self): #method that return's power cunsumption on one powerPlug
        return float(self.powerMeter)
    def turnOn(self):
        self.state = True
    def turnOff(self):
        self.state = False
    def getState(self):
        return self.state

class rgbLight(Light):
    def __init__(self):
        Light.__init__(self)
        self.color = '#ffffff' #hex code that indicates which color will the diodes emit default value #ffffff
    def setColor(self,color):
        self.color = color
    