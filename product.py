#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 15, 2021
# The program uses a loop to enter each num into a list of integers.
# When the user enters -1, the loop stops. It then calls a function that
# accepts a list of integers and returns the product of all the numbers
# entered.

def calc_product(list_of_num):

    # calculate the product in the list
    total = 1

    # calculate product of the list
    for number in list_of_num:
        total = total*number
    try:
        product = total
    except ZeroDivisionError:
        # Checks to see if the list is empty
        product = -1
    return product


def main():
    # initilizations
    # Create empty list
    list_num = []

    print("This program calculates the product of different numbers.")
    print("")

    while True:
        user_num_string = input("Enter a number between 0 to 100. Enter"
                                " -1 to stop: ")

        try:
            user_num_int = float(user_num_string)

            if (user_num_int == -1):
                print("Thank you for your input")
                break
            else:
                # add num to the list
                list_num.append(user_num_int)
        except ValueError:
            print("{} is not a valid number.". format(user_num_string))
            print("")
        else:
            user_product = calc_product(list_num)
            # user_product = round(user_product)

            if (user_product == -1):
                print("Cannot calculate the product of an empty list")
            else:
                print("Here is the list of nums: {}". format(list_num))
                print("The product is: {:.2f}". format(user_product))


if __name__ == "__main__":
    main()
