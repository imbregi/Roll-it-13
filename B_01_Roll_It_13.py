# checks input yes (y) or no (n)
def yes_no(question):
    while True:

        response = input(question).lower()
        # Checks input, question repeats if input is invalid
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no")

    # Main routine
    print("R🎲ll It 13")


# Displays instructions
def instruction():
    print('''
**** Instructions ****

Do something
and then do something else
etc
    ''')


# Checks that input is an integer that is greater than 13
def int_checker():
    while True:

        error = "Please enter an integer that is 13 or higher"

        try:
            response = int(input("Enter an integer  "))
            # Checks if integer is greater than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# loop for testing

want_instructions = yes_no("Do you want to read the instructions?")
if want_instructions == "yes":
    instruction()
print()
target_score = int_checker()
