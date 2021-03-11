class powerPlug:
    def __init__(self):
        self.state = False #state indicates if power plug get's electricity or not
        self.powerMeter = 0 #attribute that count's power Consumption in kW/h
    def turnOn(self):
        self.state = True
        self.meterEletricity() #when powerplug is on it starts metering consumption
    def turnOff(self):
        self.state = False
    def getPowerConsumption(self): #method that return's power cunsumption on one powerPlug
        return float(self.powerMeter)
    
    def countEletricity(self): #this method shall be made in a way that works in background when ever power plug is on it shall meter powerconsumption and add it to self.powerMeter
        return 1