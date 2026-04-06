import csv
import os

FILE_NAME = "clients.csv"

def load_clients():
    clients = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert types
                    row["id"] = int(row["id"])
                    row["age"] = int(row["age"])
                    clients.append(row)
        except Exception as e:
            print("Error loading file:", e)

    return clients


def save_clients(clients):
    try:
        with open(FILE_NAME, mode="w", newline="") as file:
            fieldnames = ["id", "name", "age", "plan", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(clients)

    except Exception as e:
        print("Error saving file:", e)
