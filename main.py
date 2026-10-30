
from array_stack import ArrayStack
from array_queue import ArrayQueue
from linked_stack import LinkedStack
from linked_queue import LinkedQueue


def run_structure(structure, kind):
    """Run operations for the selected data structure."""

    while True:
        if kind == "stack":
            print("\n1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Check empty")
            print("5. Check full")
            print("6. Display")
            print("7. Back")

        else:
            print("\n1. Enqueue")
            print("2. Dequeue")
            print("3. Peek front")
            print("4. Check empty")
            print("5. Check full")
            print("6. Display")
            print("7. Back")

        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                item = input("Enter an item: ")
                if kind == "stack":
                    structure.push(item)
                else:
                    structure.enqueue(item)

            elif choice == "2":
                if kind == "stack":
                    print("Popped:", structure.pop())
                else:
                    print("Dequeued:", structure.dequeue())

            elif choice == "3":
                if kind == "stack":
                    print("Top item:", structure.peek())
                else:
                    print("Front item:", structure.peek_front())

            elif choice == "4":
                print("Empty:", structure.is_empty())

            elif choice == "5":
                print("Full:", structure.is_full())

            elif choice == "6":
                print(structure)

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        print("Current state:", structure)


def main():
    while True:
        print("\n===== STACKS AND QUEUES =====")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Array Queue")
        print("4. Linked Queue")
        print("5. Exit")

        choice = input("Choose a structure: ").strip()

        if choice == "1":
            run_structure(ArrayStack(), "stack")

        elif choice == "2":
            run_structure(LinkedStack(), "stack")

        elif choice == "3":
            run_structure(ArrayQueue(), "queue")

        elif choice == "4":
            run_structure(LinkedQueue(), "queue")

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
