# Let's assume any input given by the user will always be a string.
# It returns the full name formated. 

first_name = input("What is your first name? \n> ")
last_name = input("What is your last name? \n> ")
full_name = f"{first_name} {last_name}".title()
print(full_name)
