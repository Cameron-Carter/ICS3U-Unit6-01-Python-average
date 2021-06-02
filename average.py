#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on June 2021
# This program finds the average of 10 random numbers

import random


def main():
    # This function averages 10 numbers

    random_numbers = []

    # Process and output
    for loop_counter in range(0, 10):
        generated_number = random.randint(1, 100)
        random_numbers.append(generated_number)
    average = 0
    for loop_counter in range(len(random_numbers)):
        print("Random number {0} is {1}.".format(
            loop_counter + 1, random_numbers[loop_counter]
        ))
        average += random_numbers[loop_counter]
    average = average / len(random_numbers)
    print("\nThe average is {}.".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
