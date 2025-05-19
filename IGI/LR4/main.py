# Lab Work 4: Main file
# Version: 1.0
# Developer: Belavusau Anton
# Date: May 10, 2025

import task1
import task2
import task3
import task4
import task5
import initializers_old_lab

def main():
    """Main function to run the lab work."""
    while True:
        print("\nLab Work 4 Menu:")
        print("1. Task 1: Phone Book")
        print("2. Task 2: Text Analysis")
        print("3. Task 3: Lab 3 Enhancement")
        print("4. Task 4: Rhombus Drawing")
        print("5. Task 5: Matrix Operations")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")
        try:
            if choice == '1':
                phone_book = task1.PhoneBook()
                phone_book.add_subscriber(task1.Subscriber("Biba", "12345"))
                phone_book.add_subscriber(task1.Subscriber("Boba", "1239876543"))
                phone_book.add_subscriber(task1.Subscriber("Oba", "2239876543"))
                phone_book.save_to_csv("phonebook.csv")
                phone_book.save_to_pickle("phonebook.pkl")
                prefix = input("Enter phone prefix to search: ")
                results = phone_book.search_by_phone_prefix(prefix)
                for sub in results:
                    print(sub)

            elif choice == '2':
                task2.analyze_text("input.txt", "output.txt")

            elif choice == '3':
                data = initializers_old_lab.initialize_list_input()
                stats = task3.enhance_lab3(data)
                print("Statistics:", stats)

            elif choice == '4':
                d1 = float(input("Enter diagonal 1: "))
                d2 = float(input("Enter diagonal 2: "))
                color = input("Enter color: ")
                label = input("Enter label: ")
                rhombus = task4.Rhombus(d1, d2, color, label)
                print(rhombus.get_info())
                rhombus.draw()

            elif choice == '5':
                n = int(input("Enter number of rows: "))
                m = int(input("Enter number of columns: "))
                results = task5.matrix_operations(n, m)
                print("Results:", results)

            elif choice == '6':
                break
            
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()