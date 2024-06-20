import random

# I have no more time left right now so I will have to leave it this way for now
# Current behavior: The entire tuple--e.g (<string>, <boolean>)--needs to be entered
# to be recognized as a value of the list, and that's NOT ideal

# will see how that can be improved in the current context where tuples are being used
# it might be a lot easier/straightforward to use a dictionary, using the name as the key and
# the boolean as the value O_o

guests_list = [("Pipi", False), ("Pepe", False), ("Popo", False)]
alternative_guests_list = [("Pupu", False), ("Papo", True), ("Popa", True)]

# Prompt asking for more people
while True:
    user_input = input("Enter the name of a new person: ('done' for finishing)\n> ").strip()
    if not user_input:
        continue
    elif user_input == "done":
        break
    else:
        new_guest = (user_input, random.choice([True, False]))
        guests_list.append(new_guest)
        print(f"New guest: {new_guest} added.")

    user_confirmation = input("Continue? (Y/n)").strip().lower()
    if user_confirmation == "y":
        continue
    else:
        break
    # no se puede: continue if user_confirmation == "y" else break

# Prompt asking for deleting people
while True:
    print(f"\nList: {guests_list}")
    user_input = input("Enter the name of a person you want to remove: ('done' for finishing)\n> ").strip()
    if not user_input:
        continue
    elif user_input == "done":
        break

    person = user_input
    if person not in guests_list:
        print(f"{person} is not in the guests list.")
        continue

    guests_list.remove(person)
    print(f"Removed guest: {new_guest}")

    user_confirmation = input("Continue? (Y/n)").strip().lower()
    if user_confirmation == "y":
        continue
    else:
        break
    # no se puede: continue if user_confirmation == "y" else break


verified_list = False
while not verified_list:
    # While loop will end once all values for guests_list == True
    print("Verifying list...")
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