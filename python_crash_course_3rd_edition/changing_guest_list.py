guests_list = [("Pipi", False), ("Pepe", False), ("Popo", False)]
alternative_guests_list = [("Pupu", False), ("Papo", True), ("Popa", True)]

verified_list = False

while not verified_list:
    # While loop will end once all values for guests_list == True
    verified_list = all(value for _, value in guests_list)

    # Inviting people
    print("\nPrinting list:")
    for guest in guests_list:
        print(f"* {guest[0]} was invited.")

    # Seeking confirmation
    print("\nSeeking confirmation")
    for guest in guests_list:
        if not guest[1]:
            print(f"- {guest[0]} can't make it")
            guests_list.remove(guest)

            if not alternative_guests_list:
                print("-- There are no alternative guests left to invite.")
                continue
            new_guest = alternative_guests_list.pop(-1)
            guests_list.append(new_guest)
            print(f"-- New guest {new_guest[0]} has been invited.")
        else:
            print(f"- {guest[0]} accepted your invite.")

print("\nList verified!")
print(f"Final guests list:\n{guests_list}")