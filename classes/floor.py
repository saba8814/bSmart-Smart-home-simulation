from .room import Room
class Floor:
    def __init__(self, level):
        self.id = level
        self.rooms = []
    def getNrOfRooms(self):
        return len(self.rooms)
    def turnOffEverything(self): #turn off everything on one floor
        for room in self.rooms:
            for appliance in room.appliances:
                appliance.turnOff()
    def floorPowerConsumption(self):
        consumption = 0
        for room in self.rooms:
            consumption = consumption + room.roomPowerConsumption()
        return consumption
    def getFloorLevel(self):
        return self.id