## Exercise 1: Pizza Toppings :ballot_box_with_check:

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

# print a message saying you’ll add that topping to their pizza.

print("\nWelcome to my Pizza Shop!\n")

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping == 'quit':
        print("You have finished adding toppings to your pizza.")
        break

    print(f"Adding {topping} to your pizza.")