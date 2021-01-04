import abc
from typing import Dict, List


class RoomOpening(abc.ABC):
    def __init__(self, posx: float, posy: float, width: float, height: float):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height


class Room:
    TYPE_VALID = {'BEDROOM', 'KITCHEN', 'LIVINGROOM', 'EATINKITCHEN', 'STOREROOM', 'TOILET', 'BATHROOM', 'CORRIDOR'}
    ORIENT_VALID = {'NORTH', 'SOUTH', 'EAST', 'WEST'}

    def __init__(self, type: str, area: float):
        self.type = type
        self.area = area
        self.openings = {}
        self.openings: Dict[str, List[RoomOpening]]
        if self.type not in Room.TYPE_VALID:
            raise ValueError('Invalid Room Type')

    def __repr__(self):
        return f'Room, type: {self.type}, area: {self.area}'

    def add_opening(self, orientation: str, opening: RoomOpening):
        if orientation not in Room.ORIENT_VALID:
            raise ValueError('Invalid Orientation')
        if orientation in self.openings:
            self.openings[orientation].append(opening)
        else:
            self.openings[orientation] = [opening]


class Window(RoomOpening):
    windows = []

    def __init__(self, posx: float, posy: float, width: float, height: float, can_be_opened: bool):
        super().__init__(posx, posy, width, height)
        self.can_be_opened = can_be_opened
        Window.windows.append(self)

    def __repr__(self):
        return f'Window'


class Door(RoomOpening):
    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, room2: Room):
        super().__init__(posx, posy, width, height)
        self.room1 = room1
        self.room2 = room2

    def __repr__(self):
        return f'Door between {self.room1.type} & {self.room2.type}'


class HouseDoor(Door):
    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, security_door: bool,
                 room2=None):
        super().__init__(posx, posy, width, height, room1, room2)
        self.security_door = security_door

    def __repr__(self):
        return f'HouseDoor from {self.room1.type}'


class BalconyDoor(Door):
    def __init__(self, posx: float, posy: float, width: float, height: float, room1: Room, tiltable: bool, room2=None):
        super().__init__(posx, posy, width, height, room1, room2)
        self.tiltable = tiltable

    def __repr__(self):
        return f'Balconydoor from {self.room1.type}'


class House:
    def __init__(self):
        self.rooms = {}
        self.rooms: Dict[str, List[Room]]

    def add_room(self, room: Room):
        if room.type in self.rooms:
            self.rooms[room.type].append(room)
        else:
            self.rooms[room.type] = [room]

    # def get_window_area_facing_orientation(self, orientation: str) -> float:
    #     w = 0.0
    #     for x in self.rooms.values():
    #         for y in x:
    #             for z in y.openings.keys():
    #                 for v in range(len(y.openings[z])):
    #                     if isinstance(y.openings[z][v], Window) and z == orientation:
    #                         w += y.openings[z][v].height * y.openings[z][v].width
    #     return w

    # a more elegant version:
    def get_window_area_facing_orientation(self, orientation: str) -> float:
        w = 0.0
        for x in self.rooms.values():
            for y in x:
                for key, value in y.openings.items():
                    if key == orientation:
                        for v in value:
                            if isinstance(v, Window):
                                w += v.height * v.width
        return w

    def get_number_of_openings_in_room_type(self, type: str) -> int:
        v = 0
        for x in self.rooms[type]:
            for y in x.openings.values():
                v += len(y)
        return v

    def get_all_connected_rooms(self, room: Room) -> List[Room]:
        connected_rooms = []
        for z in room.openings.values():
            for v in range(len(z)):
                if type(z[v]) == Door:
                    if z[v].room1 not in connected_rooms and z[v].room1 != room:
                        connected_rooms.append(z[v].room1)
                    if z[v].room2 not in connected_rooms and z[v].room2 != room:
                        connected_rooms.append(z[v].room2)
        return connected_rooms


if __name__ == '__main__':
    corridor = Room("CORRIDOR", 15)
    master_bed = Room("BEDROOM", 13)
    second_bed = Room("BEDROOM", 11)
    eatin_kitchen = Room("EATINKITCHEN", 27)
    eatin_kitchen.add_opening("EAST", Window(20, 30, 50, 100, True))
    eatin_kitchen.add_opening("NORTH", Window(20, 30, 50, 100, True))
    master_bed.add_opening("NORTH", Window(22, 30, 50, 100, True))
    second_bed.add_opening("WEST", Window(25, 30, 50, 100, True))
    corridor.add_opening("EAST", HouseDoor(20, 40, 100, 200, corridor, True))

    d = Door(20, 30, 90, 200, corridor, eatin_kitchen)
    corridor.add_opening("EAST", d)
    eatin_kitchen.add_opening("WEST", d)

    d = Door(40, 30, 90, 200, master_bed, corridor)
    corridor.add_opening("WEST", d)
    master_bed.add_opening("EAST", d)
    d = Door(70, 30, 90, 200, second_bed, corridor)
    corridor.add_opening("WEST", d)
    second_bed.add_opening("EAST", d)

    h = House()
    h.add_room(corridor)
    h.add_room(master_bed)
    h.add_room(second_bed)
    h.add_room(eatin_kitchen)

    print(h.rooms)
    print(master_bed.openings)

    print(h.get_window_area_facing_orientation('WEST'))
    print(h.get_number_of_openings_in_room_type('EATINKITCHEN'))
    print(h.get_all_connected_rooms(corridor))
