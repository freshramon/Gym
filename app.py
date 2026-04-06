from servicios import *
from archivos import load_clients

def menu():
    print("\n==== GYM CLIENT MANAGEMENT ====")
    print("1. Create client")
    print("2. List clients")
    print("3. Search client")
    print("4. Update client")
    print("5. Delete client")
    print("6. Exit")


def main():
    clients = load_clients()

    while True:
        menu()
        try:
            option = int(input("Choose an option: "))

            if option == 1:
                create_client(clients)
            elif option == 2:
                list_clients(clients)
            elif option == 3:
                search_client(clients)
            elif option == 4:
                update_client(clients)
            elif option == 5:
                delete_client(clients)
            elif option == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
