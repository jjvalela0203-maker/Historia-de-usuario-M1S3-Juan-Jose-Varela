# User History M1S2 📦 Inventory Management System (Python)

## 📌 Overview

This project is a simple inventory management system developed in Python.
It allows users to register multiple products, display the inventory, and calculate basic statistics using a menu-driven interface.

The program applies fundamental programming concepts such as:

* Control flow (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Lists and dictionaries
* Modular programming (separate files for logic)

---

## 🎯 Features

* Add new products to the inventory
* Display all stored products
* Calculate inventory statistics
* Input validation to prevent runtime errors
* Interactive menu that runs until the user exits

---

## 🧱 Project Structure

```
project/
│
├── main.py                  # Main program (menu and flow control)
├── modulo_inventario.py    # Inventory management functions
├── modulo_estadisticas.py  # Inventory statistics calculations
├── validaciones.py         # Input validation functions
└── README.md               # Project documentation
```

---

## 🛠️ How It Works

### 1. Add Product

The user enters:

* Product name
* Price
* Quantity

Each product is stored as a dictionary:

```
{"nombre": "Product", "precio": 1000, "cantidad": 5}
```

---

### 2. Show Inventory

Displays all products using a loop in the format:

```
Product: Laptop | Price: 2000 | Quantity: 3
```

---

### 3. Calculate Statistics

The system calculates:

* Total inventory value (price × quantity)
* Total number of products registered
* Total number of units

---

### 4. Menu System

The program runs inside a `while` loop until the user selects the exit option.

---

## 🧪 Input Validation

The system prevents invalid inputs such as:

* Empty product names
* Negative or zero values
* Non-numeric input for price or quantity
* Invalid menu options

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3 recommended)
2. Open a terminal in the project folder
3. Run:

```
python main.py
```

---

## 🧠 Concepts Applied

* Functions and modular design
* Data structures (lists and dictionaries)
* Error handling (`try/except`)
* User input validation
* Loop control and menu systems

---

## 📌 Weekly Objective

The goal of this project was to practice control structures and data handling in Python by building a functional and interactive inventory system.

---

## 👨‍💻 Author: Juan Jose Varela

Developed as part of a programming practice assignment.
