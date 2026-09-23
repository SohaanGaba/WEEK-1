
room = input("Enter current room (A or B): ").strip().upper()
status = input("Is the floor dirty? (yes/no): ").strip().lower()
if status == "yes":
    print(f"Room {room} is dirty -> Action: Clean the floor")
else:
    if room == "A":
        print(f"Room {room} is clean -> Action: Move Right to Room B")
    else:
        print(f"Room {room} is clean -> Action: Move Left to Room A")