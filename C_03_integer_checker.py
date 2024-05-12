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


# Main
target_score = int_checker()
print(target_score)