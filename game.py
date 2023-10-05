from room import Room

def play_game():
    room1 = Room("Room 1", "You are in the first room.", north=None, south=None, east="room2", west=None)
    room2 = Room("Room 2", "You are in the second room.", north=None, south=None, east=None, west="room1")

    current_room = room1

    print("Welcome to the Text-Based Adventure Game!")
    print("Type 'q' to quit.")

    while True:
        print("\n" + current_room.name)
        print(current_room.description)
        
        user_input = input("Where do you want to go? (north, south, east, west): ").lower()
        
        if user_input == 'q':
            print("Thanks for playing!")
            break

        if user_input in ['north', 'south', 'east', 'west']:
            next_room = getattr(current_room, user_input)
            if next_room:
                current_room = next_room
            else:
                print("You can't go that way.")

