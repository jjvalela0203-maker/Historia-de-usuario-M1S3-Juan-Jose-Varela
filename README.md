# 📦 Inventory Management System (Python CLI)

## 📖 Description

This is a Command Line Interface (CLI) Inventory Management System built in Python.  
It allows users to manage products efficiently by performing CRUD operations (Create, Read, Update, Delete), as well as saving and loading data using CSV files.

The system is modularized into multiple files to ensure clean code structure, readability, and scalability.

---

## 🚀 Features

- Add new products  
- Display full inventory  
- Search products by name  
- Update product details (price and quantity)  
- Delete products  
- View inventory statistics:
  - Total number of products  
  - Total units  
  - Total inventory value  
  - Most expensive product  
  - Product with highest stock  
- Save inventory to CSV  
- Load inventory from CSV (with validation)  

---

## 🗂️ Project Structure

```
.
├── app.py         # Main program (menu and execution flow)
├── services.py    # Business logic (CRUD operations & statistics)
├── archives.py    # CSV persistence (save & load data)
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x  
- No external libraries required (only standard library)

---

## ▶️ How to Run

1. Clone this repository or download the files:

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

2. Run the program:

```bash
python app.py
```

---

## 🧠 How It Works

The program runs in a loop displaying an interactive menu where the user selects options from 1 to 9:

| Option | Action |
|--------|--------|
| 1 | Add product |
| 2 | Show inventory |
| 3 | Search product |
| 4 | Update product |
| 5 | Delete product |
| 6 | Show statistics |
| 7 | Save to CSV |
| 8 | Load from CSV |
| 9 | Exit |

---

## 📁 CSV Format

The system uses a strict CSV format:

```
name,price,quantity
Laptop,1500,5
Mouse,25,10
```

### ✔️ Validation Rules:
- Must include header: `name,price,quantity`
- Price must be a float ≥ 0  
- Quantity must be an integer ≥ 0  
- Invalid rows are automatically ignored and counted  

---

## 🛡️ Error Handling

The system includes basic error handling for:
- Invalid user input  
- File not found  
- Permission errors  
- Incorrect CSV format  
- Invalid data types  

---

## 🧩 Design Highlights

- Modular architecture (separation of concerns)  
- Reusable functions  
- Input validation  
- User-friendly CLI interface  
- Cross-platform screen clearing  

---

## 📌 Future Improvements

- Add product categories  
- Implement persistent database (SQLite)  
- Add user authentication  
- Improve UI (GUI or web version)  

---

## 👨‍💻 Author: Juan Jose Varela

Developed as a Python practice project focused on:
- File handling  
- Modular programming  
- Clean code practices  
- CLI interaction  
---
