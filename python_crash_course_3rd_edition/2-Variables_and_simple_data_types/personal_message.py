name = input("Type the name of the person you want to send a message:\n> ")
content = input("Type the content of the message:\n> ")

message = f"Hi {name.strip().title()},\n\n{content}\n\nRegards,"
print(message)
