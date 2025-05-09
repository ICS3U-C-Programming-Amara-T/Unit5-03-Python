#!/usr/bin/env python3

# Created By: Amara Tie

# Date: May 9, 2025

# This is a program gets the sum of a number


def calc_grade(level):
    # defining the function
    if level == "4++":
        return 97
    elif level == "4+":
        return 95
    elif level == "4":
        return 90
    elif level == "4-":
        return 84
    elif level == "3+":
        return 78
    elif level == "3":
        return 74
    elif level == "3-":
        return 71
    elif level == "2+":
        return 68
    elif level == "2":
        return 64
    elif level == "2-":
        return 61
    elif level == "1+":
        return 56
    elif level == "1":
        return 54
    else:
        return -1


def main():
    # Ask User for a number
    level = input("Enter a your grade level e.g (4, 3+, 2-) :")
    print("")

    # Call function and calculate grade level
    grade = calc_grade(level)
    if grade == -1:
        print("Invalid grade")
    else:
        print(f"The level {level} is {grade}%")


if __name__ == "__main__":
    main()
