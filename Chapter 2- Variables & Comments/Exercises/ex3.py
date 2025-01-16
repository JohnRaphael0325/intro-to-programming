## Exercise 3: Stripping Names :ballot_box_with_check:

# Tidy up the code to make it easier to understand

# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

# Print the name once, so the whitespace around the name is displayed. 

# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "\n\tJohn Raphael\n\t"

print("\nPrint the name with left side stripped") 
print(name.lstrip())
print("\nPrint the name with right side stripped") 
print(name.rstrip())
print("\nPrint the name with both sides stripped")
print(name.strip())