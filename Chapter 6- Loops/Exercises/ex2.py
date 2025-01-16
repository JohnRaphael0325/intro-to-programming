## Exercise 2: Movie Tickets: :ballot_box_with_check:

# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

# they are between 3 and 12, the ticket is $10; and 
# if they are over age 12, the ticket is $15. Write a loop in which you ask users their 

# age, and then tell them the cost of their movie ticket

print("\nWelcome to the Cinema\n")
print("Prices for Tickets:")
print("0-2 = Free")
print("3-12 = $10")
print("Over 12 = $15\n")

while True:
    age = input("Please enter your age (or type 'quit' to exit): ")

    if age == 'quit':
        print("Thank you! Have a great day!")
        break

    age = int(age)

    if age < 3:
        print("Your movie ticket is free!")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")
    