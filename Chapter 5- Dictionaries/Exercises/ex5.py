## Exercise 5: Pets :ballot_box_with_check:

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

# owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

# each pet

pets = [
    {"name": "Buddy", "kind": "dog", "owner": "Alice"},
    {"name": "Mittens", "kind": "cat", "owner": "Bob"},
    {"name": "Goldie", "kind": "fish", "owner": "Charlie"},
    {"name": "Coco", "kind": "parrot", "owner": "Diana"},
    {"name": "Thumper", "kind": "rabbit", "owner": "Ethan"}
]

for pet in pets:
    print(f"Information about {pet['name']}:")
    print(f"  Name: {pet['name']}")
    print(f"  Kind: {pet['kind']}")
    print(f"  Owner: {pet['owner']}")