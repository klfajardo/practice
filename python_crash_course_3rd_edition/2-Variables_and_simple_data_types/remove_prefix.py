# Remove given prefix from given string
# Si ingreso un prefijo que no existe en el given string, directamente deja el string igual

user_input = input("Type the String you want to remove the prefix\n> ")
clean_input = user_input.strip().lower()

prefix = input("Type the prefix\n> ")
removed_prefix_input = clean_input.removeprefix(prefix)

print("  " + removed_prefix_input)
