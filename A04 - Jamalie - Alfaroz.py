######################################################################
# Author: Ela Jamali, Emely Alfaro Zavala
# Username: jamalie, Alfaroe
#
# Purpose: Learn the impact a bug can have in the real world.
# Explore life path numbers.
# Practice creating your own fruitful functions.
# Learn to use modulus to capture remainders.
#
######################################################################
# Acknowledgements: Aaron Christon (TA hours) and Eureka (the moment Ela had when she figured out the first function)
######################################################################
import turtle


def day_of_birth():
    """
    this function first checks if the input is a master number (11,22,33) and returns it. if not a master number, it adds the integers of the day of birth and returns them.
    :param: None
    :return: sum of integers of the day of birth or master number (11, 22 or 33)
    """
    day = (int(input("What is the day of your birthday?")))    # asks the user to input their day of birth
    if day % 11 == 0 and day <= 33:                            # checks if input is a master number by dividing it by 11 and checking if it is less than 33
        return day                                             # if the conditions are met, the master number is return (11,22,33)
    else:
        n = day % 10                                           # defining variable n and using modulus to get the second value to sum
        m = day // 10                                          # defining variable m and using floor division to get to get the first value to sum
        return m + n                                           # adding the two variables


def month_of_birth():
    """
    this function first checks if the input is a master number (11,22,33) and returns it. if not a master number, it adds the integers of the month of birth and returns them.
    :param: None
    :return: sum of integers of the month of birth or master number (11, 22 or 33)
    """
    month = (int(input("What is the month of your birthday?")))   # asks the user to input their month of birth
    if month % 11 == 0 and month <= 33:                           # checks if input is a master number by dividing it by 11 and checking if it is less than 33
        return month                                              # if the conditions are met, the master number is return (11,22,33)
    else:
        n = month % 10                                            # defining variable n and using modulus to get the second value to sum
        m = month // 10                                           # defining variable m and using floor division to get to get the first value
        return m + n                                              # adding the two variables


def year_of_birth():
    """
    this function gets the year if the sum of the digits of the year is a master number (11,22,33) it keeps it and returns it. if not a master number, it adds the integers of the year of birth and returns them.
    :param: None
    :return: sum of integers of the year of birth or master number (11, 22 or 33)
    """
    year = (int(input("What is the year of your birthday?")))     # asks the user to input their year of birth
    if year % 11 == 0 and year <= 33:                             # checks if input is a master number by dividing it by 11 and checking if it is less than 33
        return year                                               # if the conditions are met, the master number is return (11,22,33)
    else:
        f1 = year // 1000                                         # using floor division by 1000 to get first integer for year
        f2 = year % 1000                                          # reducing the year to hundreds so we can get second digit
        s1 = f2 // 100                                            # using floor division by 100 to get second integer for year
        s2 = f2 % 100                                             # reducing the year to tents so we can get third digit
        t1 = s2 // 10                                             # using floor division by 10 to get third integer for year
        t2 = s2 % 10                                              # reducing the year to tents so we can get remainder (fourth digit)
        suma = f1 + s1 + t1 + t2                                  # adding all the variables previously found so we get the total for year
        if suma >= 10 and suma % 11 != 0:                         # we calculate here if our value is equal or less than ten and aif the remainder of dividing it by 11 is not zero
            return suma % 10 + suma // 10                         # if the conditions are met, we take the reminder of suma/10 and add it to the floor division of that number and 10
        else:
            return suma                                           # if the final value does not meet the conditions, it is returned as it is.


def life_path_number():
    """
    function that first calls all the functions and then adds all their values found to get the final life path number
    :param: None
    :return: sum of the three values found
    """
    day1 = day_of_birth()                                        # assigning the day_of_birth function to a variable to get its value
    month1 = month_of_birth()                                    # assigning the month_of_birth function to a variable to get its value
    year1 = year_of_birth()                                      # assigning the year_of_birth function to a variable to get its value
    number = day1 + month1 + year1                               # adding the three values together to get the life path number
    if number >= 10 and number % 11 != 0:                        # if the number found is equal or more than 10 and its reminder is other than zero then
        return number % 10 + number // 10                        # the reminder of dividing the number by then and the one of doing floor division by ten is added.
    else:
        return number                                            # if those conditions are not met, the total amount (number) is returned.


def final(tortuga):
    """
    This function will display the life path number using turtle
    :param: tortuga = a turtle object
    :return: None
    """
    numero = life_path_number()   # we adding a value to the variable numero which will call the life_path_number
    tortuga.write("Congratulations. Your life path number is " + str(numero), move=False, align="center", font=("Arial", 23, "italic"))
    # the turtle will write the statement based on the life path number in a specific font and position


def main():
    """
    main function where other functions are executed to find the life path number
    :param: None
    :return: None
    """
    tortuga = turtle.Turtle()                  # creating a turtle object
    tortuga.shape("blank")                     # hiding the turtle object in the middle of the screen.
    tortuga.pencolor("black")                  # changing the pen color to black so the turtle writes in that color

    wn = turtle.Screen()                       # setting up the background for our turtle object
    wn.bgpic("backg.gif")                      # inserting an image in the background
    wn.bgcolor("purple")                       # setting the color of the background
    final(tortuga)                             # calling our final function that runs the other functions to compute life path number
    wn.exitonclick()                           # indicates that the screen will exit when we click it


main()



