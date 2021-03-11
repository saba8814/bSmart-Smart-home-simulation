from classes.audio import Audio
from classes.house import House
from classes.lights import * 
from classes.powerPlug import powerPlug
from classes.floor import Floor
from classes.room import Room


nrOfFloors = int(input('please input number of floors in your house '))
house = House(nrOfFloors)

for i in range(0,nrOfFloors):
    house.floors.append(Floor(i))

for level in house.floors:
    nrOfRooms = int(input('please input number of roooms on floor number ' +  str(level.getFloorLevel()+1) + ' in your house '))
    for i in range(0,nrOfRooms):
        nameOfTheRoom = input('input name of the room nr ' + str(i+1) + ' on floor nr ' + str(level.getFloorLevel() + 1)+' ')
        level.rooms.append(Room(nameOfTheRoom))
for i in range(0,house.getNrOfFloors()):
    for j in range(0,house.floors[i].getNrOfRooms()):
        nrOfAppliances = int(input('enter number of appliances in room  ' + str(house.floors[i].rooms[j].name) + ' on floor number' + str(i + 1))+ ' ')
        for k in range(0,nrOfAppliances):
            print('to add light press 1 ')
            print('to add rgb light press 2 ')
            print('to add powerplug press 3 ')
            select = int(input())
            if select==1:
                house.floors[i].rooms[j].addAppliance(Light())
            if select==2:
                house.floors[i].rooms[j].addAppliance(rgbLight())
            if select==3:
                house.floors[i].rooms[j].addAppliance(powerPlug())
#i've made registration part further on you can play with the program on Your own for example following line turns off everything on floor nr 1
house.floors[0].turnOffEverything()

