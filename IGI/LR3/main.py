"""
Lab Work 1
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
Description: Main module to test functions from tasks 1-5.
"""

import task1
import task2
import task3
import task4
import task5
from validator import handle_input
from initializers import initialize_list_generator, initialize_list_input

def display_menu():
    """Display the main menu options."""
    print("\n--- Main Menu ---")
    print("1. Task 1: Series Computation")
    print("2. Task 2: Count Negative Numbers")
    print("3. Task 3: Binary String Check")
    print("4. Task 4: String Analysis")
    print("5. Task 5: List Operations")
    print("0. Exit")

def main():
    """Main function to run the program."""
    is_running = True
    while is_running:
        display_menu()
        choice = handle_input(
            "Choose an option (0-5): ",
            lambda x: x.strip() in {'0', '1', '2', '3', '4', '5'}
        )

        if choice == '1':
            x = float(handle_input("Enter x: ", lambda x: True))
            eps = float(handle_input("Enter epsilon: ", lambda x: float(x) > 0))
            result = task1.compute(x, eps)
            print(f"Result: {result[0]}, Iterations: {result[1]}")
        elif choice == '2':
            print("Enter numbers (stop with >100):")
            count = task2.compute()
            print(f"Negative numbers count: {count}")
        elif choice == '3':
            s = handle_input("Enter a string: ", lambda x: True)
            is_binary = task3.compute(s)
            print(f"Is binary: {is_binary}")
        elif choice == '4':
            s = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
            result = task4.compute(s)
            print(f"Lowercase letters: {result[0]}, Word with 'v': {result[1]}, Filtered string: {result[2]}")
        elif choice == '5':
            print("Choose: ")
            print("1. Generate sequence")
            print("2. Input sequence")
            cchoice = int(handle_input("", lambda c : c.strip() in ["1", "2"]))
            arr = []
            if (cchoice == 1):
                n = int(handle_input("Enter size of list: ", lambda x: True))
                arr = [val for val in initialize_list_generator(n)]
            elif (cchoice == 2):
                print("Initialize list: ")
                arr = initialize_list_input()
                
            if (cchoice == 1 or cchoice == 2):
                try:
                    mult, sum_zeros = task5.compute(arr)
                    print(f"Product: {mult}, Sum between zeros: {sum_zeros}")
                except ValueError as e:
                    print(e)
            
        elif choice == '0':
            is_running = False

if __name__ == "__main__":
    main()