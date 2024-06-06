locations = ["Japon", "Noruega", "Peru", "Espa;a", "Alemania"]
print(f"List in original order: {locations}")

print(f"\nList sorted : {sorted(locations)}")
print(f"List is still in its original order: {locations}")


print(f"\nList sorted in reverse: {sorted(locations, reverse=True)}")
print(f"List is still in its original order: {locations}")

locations.reverse()
print(f"\nList reversed: {locations}")
locations.reverse()
print(f"List in original order: {locations}")

locations.sort()
print(f"\nList stored and sorted: {locations}")
