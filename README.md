# 🏋️ Gym Client Management System (CSV-Based)

## 📌 Project Overview

The **Gym Client Management System** is a console-based application developed in Python that allows administrative staff to efficiently manage client information.

The system supports full CRUD operations (Create, Read, Update, Delete) and uses a **CSV file for data persistence**, ensuring that client information is maintained between program executions.

---

## 🎯 Objective

To provide a simple, modular, and efficient solution for managing gym clients, including their personal information, subscription plans, and status.

---

## ⚙️ Features

* ✅ Create new clients
* 📋 List all registered clients
* 🔍 Search clients by ID or name
* ✏️ Update client information
* ❌ Delete clients
* 💾 Persistent storage using CSV files

---

## 🧱 Data Structure

Each client is stored as a dictionary with the following structure:

```
{
    "id": int,
    "name": str,
    "age": int,
    "plan": str,        # monthly, quarterly, annual
    "status": str       # active or inactive
}
```

---

## 📁 Project Structure

```
gym_system/
│
├── app.py         # Main program (user interaction)
├── servicios.py   # Business logic (CRUD operations)
├── archivos.py    # File handling (CSV persistence)
└── clients.csv    # Data storage (auto-generated)
```

---

## 🖥️ How to Run

1. Make sure you have Python installed (version 3.x).
2. Download or clone the project.
3. Open a terminal in the project folder.
4. Run the application:

```
python app.py
```

---

## 📊 Menu Options

```
1. Create client
2. List clients
3. Search client
4. Update client
5. Delete client
6. Exit
```

---

## 💾 Data Persistence

* The system uses a file named `clients.csv`.
* If the file does not exist, it will be created automatically.
* Data is saved after every operation (create, update, delete).
* Data is loaded automatically when the program starts.

---

## 🧪 Error Handling

The system includes basic error handling:

* Validation of numeric inputs (ID, age)
* Prevention of duplicate IDs
* Handling of invalid menu options
* Try/except blocks to avoid crashes

---

## 🧠 Design Principles

### 🔹 Modular Design

The project is divided into three main modules:

* **app.py** → Handles user interaction and menu navigation
* **servicios.py** → Contains all business logic (CRUD operations)
* **archivos.py** → Manages file operations (read/write CSV)

### 🔹 Data Structures

* Lists → Store multiple clients
* Dictionaries → Represent each client

---

## 🚀 Possible Improvements

* Input validation for plan types (monthly, quarterly, annual)
* Confirmation prompts before deleting clients
* Better UI formatting (tables)
* Migration to a database (SQLite, MySQL)
* GUI implementation (Tkinter or web app)

---

## 👨‍💻 Author

Developed as part of a Python programming project focused on data structures, modular design, and file persistence.

---

## 📜 License

This project is for educational purposes only.
