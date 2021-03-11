from .audio import Audio
class Room:
    def __init__(self,name):
        self.name = name
        self.appliances = []
        self.audio = Audio()
    def addAppliance(self,appliance):
        self.appliances.append(appliance)

    def removeApplianceById(self,applianceId):
        del self.appliances[applianceId]

    def roomPowerConsumption(self):
        consumption = 0 
        for appliance in self.appliances:
            consumption = consumption + appliance.getPowerConsumption()
        return consumption