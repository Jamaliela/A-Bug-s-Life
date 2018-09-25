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
# Acknowledgements: Aaron Christon and Eureka (the moment Ela had when she figured the first function out)
######################################################################


def day_of_birth():
    """

    :param
    :return: None
    """
    day = (int(input("What is the day of your birthday?")))
    if day % 11 == 0 and day <= 33:
        return day
    else:
        n = day % 10
        m = day // 10
        return m + n


def month_of_birth():
    """

    :param
    :return: None
    """
    month = (int(input("What is the month of your birthday?")))
    if month % 11 == 0 and month <= 33:
        return month
    else:
        n = month % 10
        m = month // 10
        return m + n


def year_of_birth():
    """

    :return:
    """
    year = (int(input("What is the year of your birthday?")))
    if year % 11 == 0 and year <= 33:
        return year
    else:
        f1 = year // 1000
        f2 = year % 1000
        s1 = f2 // 100
        s2 = f2 % 100
        t1 = s2 // 10
        t2 = s2 % 10
        suma = f1 + s1 + t1 + t2
        if suma >= 10 and suma % 11 != 0:
            return suma % 10 + suma // 10
        else:
            return suma


def life_path_number():
    day1 = day_of_birth()
    month1 = month_of_birth()
    year1 = year_of_birth()
    number = day1 + month1 + year1
    if number >= 10 and number % 11 != 0:
        return number % 10 + number // 10
    else:
        return number





#
# def pp ():
#     """
#
#     :return: None
#     """
#     pass
#
# def
#     """
#
#     :param num:
#     :return:
#     """
#    pass
#
# def
#     """
#
#
#     :param
#     :return: None
#     """
#
#
# def random_peeler():
#     """
#
#     :return: None
#     """
#     pass


def main():
    """

    :return: None
    """


# day_of_birth()
# month_of_birth()
# year_of_birth()
print(life_path_number())


main()


