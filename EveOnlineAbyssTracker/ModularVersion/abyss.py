from colorama import Fore
import os
from globals import *


def abyssMain(startingIsk=None, abyssal_runs=0, total_Time=0):
    """
    Main function to track Abyssal runs and calculate profits.

    Args:
        startingIsk (float, optional): Initial ISK before Abyssal run.
        abyssal_runs (int): Number of Abyssal runs.
        total_Time (float): Total time spent in Abyssal runs.

    Returns:
        tuple: Tuple containing updated `startingIsk`, `abyssal_runs`, and `total_Time`.
    """
    global total_profit  # Use the global total_profit variable

    while True:
        try:
            if startingIsk is None:
                startingIsk = startingInven()  # Ask for starting_inv only if it's None
        except ValueError:
            os.system("CLS")
            print(f"\n{Fore.RED}Invalid choice. Please enter a Float")
            startingIsk = None
            continue

        try:
            after_inv = afterInven()
            time_in_abyss = timeSpent()
        except ValueError:
            os.system("CLS")
            print(f"\n{Fore.RED}Invalid choice. Please enter a Float")
            continue

        profit = profitCalc(startingIsk, after_inv, time_in_abyss)
        startingIsk += profit  # Update startingIsk with the profit for this run
        abyssal_runs += 1  # Increment the counter for each Abyssal run
        total_Time += time_in_abyss

        while True:
            user_input = input(
                f"{Fore.GREEN}Track another Abyssal run? (1/0): {Fore.RED}"
            ).upper()
            os.system("CLS")

            if user_input == "1":
                break  # Exit the inner loop to continue tracking another Abyssal run
            elif user_input == "0":
                print(
                    f"\n{Fore.GREEN}Total Profit: {Fore.RED}{total_profit}m"
                )  # Use total_profit here
                print(f"{Fore.GREEN}Total Abyssals Run: {
                      Fore.RED}{abyssal_runs}")
                print(f"{Fore.GREEN}Total Time Spent: {
                      Fore.RED}{total_Time} Mins\n")

                return (
                    startingIsk,
                    abyssal_runs,
                    total_Time,
                )  # Exit the function to return to the main menu
            else:
                print(f"{Fore.YELLOW}Invalid input. Please enter 1 or 0.\n")


def profitCalc(starting_inv, after_inv, TimeinsideAbyss):
    """
    Calculate profit from an Abyssal run.

    Args:
        starting_inv (float): Initial ISK before Abyssal run.
        after_inv (float): ISK after Abyssal run.
        TimeinsideAbyss (float): Time spent in Abyssal run.

    Returns:
        float: Profit from the Abyssal run.
    """
    global total_profit  # Use the global total_profit variable
    profit = after_inv - starting_inv
    new_total = starting_inv + profit
    total_profit += profit

    profit_string = (f"\n{Fore.GREEN}Profit: {Fore.RED}{profit} Million\n{Fore.GREEN}New total: {Fore.RED}{new_total}\n{Fore.GREEN}Time inside Abyss: {Fore.RED}{TimeinsideAbyss} Mins\n{Fore.GREEN}")
    print(profit_string)
    return profit  # Return the profit for the current run


def startingInven():
    """
    Get the ISK total before an Abyssal run.

    Returns:
        float: ISK total before Abyssal run.
    """
    while True:
        try:
            before = float(
                input(f"\n{Fore.GREEN}Isk Total before Abyss: {Fore.RED}"))
        except ValueError:
            os.system("CLS")
            print("Invalid Choice please enter a Float")
            continue
        return before


def afterInven():
    """
    Get the ISK total after an Abyssal run.

    Returns:
        float: ISK total after Abyssal run.
    """
    while True:
        try:
            after = float(
                input(f"{Fore.GREEN}Isk Total after Abyss: {Fore.RED}"))
        except ValueError:
            os.system("CLS")
            print("Invalid Choice please enter a Float\n")
            continue
        return after


def timeSpent():
    """
    Get the time spent in an Abyssal run.

    Returns:
        float: Time spent in Abyssal run.
    """
    global MAXTIME
    while True:
        try:
            timeLeft = float(
                input(f"{Fore.GREEN}Time Left when leaving: {Fore.RED}"))
            timeSpent = MAXTIME - timeLeft
        except ValueError:
            os.system("CLS")
            print("Invalid Choice please input a Float")
            continue
        return timeSpent
