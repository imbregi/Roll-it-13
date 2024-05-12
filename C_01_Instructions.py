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


def instruction():
    print('''
**** Instructions ****

Do something
and then do something else
etc
    ''')


# loop for testing

want_instructions = yes_no("Do you want to read the instructions?")
if want_instructions == "yes":
    instruction()
print("program")
