from archivos import save_clients

def create_client(clients):
    try:
        client_id = int(input("Enter client ID: "))

        for client in clients:
            if client["id"] == client_id:
                print("Client ID already exists.")
                return

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        plan = input("Enter plan (monthly, quarterly, annual): ").lower()
        status = input("Enter status (active/inactive): ").lower()

        client = {
            "id": client_id,
            "name": name,
            "age": age,
            "plan": plan,
            "status": status
        }

        clients.append(client)
        save_clients(clients)
        print("Client created successfully.")

    except ValueError:
        print("Invalid input.")


def list_clients(clients):
    if not clients:
        print("No clients registered.")
        return

    for client in clients:
        print(client)


def search_client(clients):
    try:
        option = input("Search by (1) ID or (2) Name: ")

        if option == "1":
            client_id = int(input("Enter ID: "))
            for client in clients:
                if client["id"] == client_id:
                    print(client)
                    return

        elif option == "2":
            name = input("Enter name: ").lower()
            for client in clients:
                if client["name"].lower() == name:
                    print(client)
                    return

        print("Client not found.")

    except ValueError:
        print("Invalid input.")


def update_client(clients):
    try:
        client_id = int(input("Enter ID to update: "))

        for client in clients:
            if client["id"] == client_id:
                print("Leave blank to keep current value.")

                name = input(f"Name ({client['name']}): ")
                age = input(f"Age ({client['age']}): ")
                plan = input(f"Plan ({client['plan']}): ")
                status = input(f"Status ({client['status']}): ")

                if name:
                    client["name"] = name
                if age:
                    client["age"] = int(age)
                if plan:
                    client["plan"] = plan.lower()
                if status:
                    client["status"] = status.lower()

                save_clients(clients)
                print("Client updated successfully.")
                return

        print("Client not found.")

    except ValueError:
        print("Invalid input.")


def delete_client(clients):
    try:
        client_id = int(input("Enter ID to delete: "))

        for client in clients:
            if client["id"] == client_id:
                clients.remove(client)
                save_clients(clients)
                print("Client deleted successfully.")
                return

        print("Client not found.")

    except ValueError:
        print("Invalid input.")
