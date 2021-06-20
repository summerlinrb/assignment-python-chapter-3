# Follow the assignment instructions to code an app that
# will tell a user their birthstone.

user_input = input("Enter the number of the month you were born (1-12)>")
month = int(user_input)

if month == 1:
    print("Your birthstone is garnet.")
elif month == 2:
    print("Your birthstone is amethyst.")
elif month == 3:
    print("Your birthstone is aquamarine.")
elif month == 4:
    print("Your birthstone is diamond.")
elif month == 5:
    print("Your birthstone is emerald.")
elif month == 6:
    print("Your birthstone is alexandrite.")
elif month == 7:
    print("Your birthstone is ruby.")
elif month == 8:
    print("Your birthstone is peridot.")
elif month == 9:
    print("Your birthstone is sapphire.")
elif month == 10:
    print("Your birthstone is pink tourmaline.")
elif month == 11:
    print("Your birthstone is topaz.")
elif month == 12:
    print("Your birthstone is blue topaz.")

else:
    print("That is not a valid number.")

# # Chapter 3.2 Conditional Statements
# print("Chapter 3.2 Conditional Statements")
# temperature = 15
# if temperature > 30:
#     print("It's Warm")
#     print("Drink Water")
# elif temperature > 20:
#     print("It's nice")

# else:
#     print("It's cold")
# print("Done")
# print("*" * 30)


# # Chapter 3.12 While Loops
# print("#Chapter 3.12 While Loops")
# command = ""
# while command.lower() != "quit":
#     command = input("Enter any command of 'quit' > ")
#     print("ECHO", command)
# print("*" * 30)
