from commands.create import create_shape
from commands.delete import delete_shape
from commands.get import list_shapes


def print_menu():
    print("\n--- Vector Editor CLI ---")
    print("1. Create shape")
    print("2. Delete shape")
    print("3. List shapes")
    print("4. Exit")


def main():
    shapes = []

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            shape_type = input("Enter shape type (point, line, circle, square): ").strip().lower()
            try:
                shape = create_shape(shape_type, shapes)
                if shape:
                    shapes.append(shape)
                    print(f"Created: {shape}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                index = int(input("Enter index to delete: ").strip())
                delete_shape(shapes, index)
                print("Shape deleted.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            list_shapes(shapes)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
