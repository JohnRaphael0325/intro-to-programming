## Exercise 4:  Large Shirts :ballot_box_with_check:

# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

# medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = "Large", message = "I love Python"):
    print(f"The shirt's size is {size} and has a message of {message}")
make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "Small", message = "My mother always used to say: The older you get, the better you get, unless you're a banana")