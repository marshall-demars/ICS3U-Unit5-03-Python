#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Dec 2022
# This program converts a level grade to middle percentage


def mark_to_percentage(mark):
    # This function converts a level mark to a percentage

    if mark == "4+":
        percentage = 97
    elif mark == "4":
        percentage = 90
    elif mark == "4-":
        percentage = 83
    elif mark == "3+":
        percentage = 78
    elif mark == "3":
        percentage = 75
    elif mark == "3-":
        percentage = 71
    elif mark == "2+":
        percentage = 68
    elif mark == "2":
        percentage = 65
    elif mark == "2-":
        percentage = 61
    elif mark == "1+":
        percentage = 58
    elif mark == "1":
        percentage = 55
    elif mark == "1-":
        percentage = 51
    elif mark == "R":
        percentage = 25
    elif mark == "NE":
        percentage = 0
    else:
        percentage = -1

    return percentage


def main():
    # this function gets the mark and catches errors

    # Input
    mark = input("Enter the mark you want converted to percentage (Ex: 3+): ")

    # Call functions
    final_percent = mark_to_percentage(mark)

    if final_percent == -1:
        print("\nInvalid Input")
    else:
        print(
            "\nLevel {0} has a middle percentage of {1}%.".format(mark, final_percent)
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
