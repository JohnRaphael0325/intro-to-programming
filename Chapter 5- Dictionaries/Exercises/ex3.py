## Exercise 3: Glossary 2 :ballot_box_with_check:
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

# calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

# to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "Variable": "Used to store a value.",
    "Function": "Reusable code that does a specific task, and can be used with its name.",
    "Loop": "A set of instructions that is repeated until a certain condition is met.",
    "Dictionary": "Stores key-value pairs, allowing efficient retrieval of values based on their keys.",
    "Boolean": "A data type that represents only two values: True or False.",
    "List": "An ordered collection of items that can be changed.",
    "Tuple": "An ordered collection of items that cannot be changed.",
    "Set": "An unordered collection of unique items.",
    "String": "A sequence of characters used to represent text.",
    "Keyword": "A reserved word in Python that has a specific meaning and cannot be used as a variable name."
}

for term, meaning in glossary.items():
    print(f"{term}:\n  {meaning}\n")
