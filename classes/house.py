class House:
    def __init__(self,nrOfFloors):
        self.floor = nrOfFloors
        self.floors = []
    def powerConsumption(self):
        consumption = 0
        for floor in self.floors:
            consumption = consumption + floor.floorPowerConsumption()
        return consumption
    def getNrOfFloors(self):
        return self.floor