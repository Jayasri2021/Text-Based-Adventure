from room import Room

def play_game():
    room1 = Room("Room 1", "You are in the first room.", north=None, south=None, east="room2", west=None)
    room2 = Room("Room 2", "You are in the second room.", north=None, south=None, east=None, west="room1")

    current_room = room1

