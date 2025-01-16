## Exercise 3: T-Shirt  :ballot_box_with_check:

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

# should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

# arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"The shirt will have the size of {size} and have the message: {message}")

make_shirt("Large", "I am a Horse")
make_shirt(size ="Medium", message = "Keep Calm and Collected.")