## Exercise 2: Glossary :ballot_box_with_check:

# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# * Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

# their meanings as values.

# * Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

# the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

# each word-meaning pair in your output.

glossary = {
    "Variable": "Used to store a value.",
    "Function": "It's reusable code that does a specific task, and can be used with it's name.",
    "Loop": "Set of instructions that is repeated until a certain condition is met.",
    "Dictionary": "This stores key-value pairs, allowing efficient retrieval of values based on their keys.",
    "Boolean": "A data type that represents only two values: True or False."
}

for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")
