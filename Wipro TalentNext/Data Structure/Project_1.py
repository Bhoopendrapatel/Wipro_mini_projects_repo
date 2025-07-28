import random

people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original List:")
for person, fact in people.items():
    print(f"{person}: {fact}")

jeff_facts = sorted(people.values())
people["Jeff"] = random.choice(jeff_facts)

people["Jill"] = "Can hula dance."

print("\nUpdated List:")
for person, fact in people.items():
    print(f"{person}: {fact}")