while True:

    error = "Please enter an integer that is 13 or higher"

    try:
        my_num = int(input("Enter an integer  "))
        # Checks if integer is greater than or equal to 13
        if my_num < 13:
            print(error)
        else:
            print("Your number is ", my_num)

    except ValueError:
        print(error)