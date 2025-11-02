# 🧮 Calculator CLI

A simple and modular command-line calculator built with Python.  
This project was developed following **Clean Code**, **SOLID principles**, and a **Test-Driven Development (TDD)** approach.

## 🧩 Projet Structure

    calculator-cli
    ├── core/                # Core logic (Calculator class)
    ├── cli/                 # Command-line Interface 
    ├── tests/               # Unit tests using pytest
    ├── .venv/               # Virtual enviroment
    ├── requirements.txt     # Project dependencies
    └── README.md            # Documentation

## ⚙️ Installation

1. Clone repository

        git clone https://github.com/GusVargas17/calculator-cli.git
        cd calculator-cli

2. Create and activate a virtual environment:

        python -m venv .venv
        source .venv/bin/activate      # Linux or macOS
        # .venv\Scripts\activate       # Windows

3. Install the dependencies:

        pip install -r requirements.txt

## 🚀 Run the Program

To start the calculator in CLI mode:

        python calculator-cli/main.py

## 🧪 Run tests

        PYTHONPATH=. pytest -v

## 💻 Technologies Used

        Python 3.13
        Pytest
        Virtual Environment (venv)
        Command-Line Interface (CLI)

## 🎯 Project Goals
        Reinforce backend development skills.
        Apply object-oriented programming and testing methodologies.
        Maintain clean, maintainable, and scalable code.

## 👤 Author

        Developed by Gustavo Vargas,
        Backend Developer in training 