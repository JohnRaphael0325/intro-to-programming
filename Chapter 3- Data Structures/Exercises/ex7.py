## Exercise 7: Seeing the World :ballot_box_with_check:
# Think of at least five places in the world you’d like to visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.

# •	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

# •	 Use sorted() to print your list in alphabetical order without modifying the actual list.

# •	 Show that your list is still in its original order by printing it.

# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

# •	 Show that your list is still in its original order by printing it again.

# •	 Use reverse() to change the order of your list. Print the list to show that its order has changed.

# •	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

# •	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# Define fav_places as a list, not a tuple

# Define fav_places as a list

# Define fav_places as a list
fav_places = ["Tokyo", "New York", "Paris", "Dubai", "Geneva"]

print("Original List:")
print(fav_places)

print("\nAlphabetical Order:")
print(sorted(fav_places))

print("\nStill in the same order:")
print(fav_places)

fav_places.reverse()
print("\nReversed Order:")
print(fav_places)

fav_places.reverse()
print("\nList after Reversed")
print(fav_places)

print("\nAlphabetical Order again:")
print(sorted(fav_places))

fav_places.sort(reverse=True)
print("\nReversed Alphabetical Order:")
print(fav_places) # Source: ChatGPT, Prompt: How to make it Reversed but also Alphabetical?
