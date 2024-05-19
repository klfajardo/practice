import random

quotes = [
        "The important thing is not to stop questioning. Curiosity has its own reason for existing",
        "I have no special talents, I am only passionately curious.",
        "Imagination is more important than knowledge.",
        "A clever person solves a problem. A wise person avoids it."] # wao!

author = "Albert Einstein"
message = f'Albert Einstein once said, "{quotes[random.randrange(0, 4)]}"'
print(message)

# https://docs.python.org/3/library/random.html
# https://www.jagranjosh.com/general-knowledge/albert-einstein-quotes-1698299107-1
