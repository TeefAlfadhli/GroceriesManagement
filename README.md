# Groceries Management System

![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.x-blue)

## Description
The **Groceries Management System** is a Python-based command-line application for managing grocery inventory. The system includes user authentication, item management, low stock notifications, expiry tracking, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Example Commands](#example-commands)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/groceries-management-system.git
   cd groceries-management-system
2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
## Usage
Run the program using the command:
```bash
python Groceries.py <command> [arguments]
```
##Login Credentials

### Manager:
- **Username**: `manager1`
- **Password**: `managerpass`

### Worker:
- **Username**: `worker1`
- **Password**: `workerpass`

## Common Commands:
- **Add an item:**
  ```bash
  python Groceries.py add "apple" 10 "fruit" 2024-12-31

- **Delete an item:**
  ```bash
  python Groceries.py delete "apple"

- **View all items (Manager only):**
  ```bash
  python Groceries.py view

- **Check expired items:**
  ```bash
  python Groceries.py check_expired
  
# Features
- User Authentication: Secure login for managers and workers.
- Item Management: Add, delete, and view items with details such as quantity, category, and expiry date.
- Low Stock Notifications: Alerts when item quantity falls below a set threshold.
- Expiry Tracking: Lists items that are past their expiry date.
- Search Functionality: Search for items by name.
- Inventory Report: Generates a summary report of total items and quantities.
- Receipts Log: Tracks all add/delete actions with timestamps.

# Example Commands
**Add an Item:**
```bash
python Groceries.py add "banana" 15 "fruit" 2024-11-30
```
**Delete an Item:**
```bash
python Groceries.py delete "banana"
```
**View All Items:**
```bash
python Groceries.py view
```
**Check for Low Stock:**
```bash
python Groceries.py check_low_stock --threshold 5
```
**Generate a Report:**
```bash
python Groceries.py report
```
# Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.
**Steps to Contribute:** 

1. Fork the repository.
2. Create a branch for your feature (git checkout -b feature/NewFeature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature/NewFeature).
5. Open a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact Information
Created by - [Teef Alfadhli](#TeefAlfadhli) – feel free to reach out via teefalfadhli9@hotmail.com

# FAQ
**Q: How do I reset the inventory?**
**A:** Delete groceries.json and rerun the add command to initialize it.
**Q: Can I run this project on Windows?**
**A:** Yes, the project is cross-platform as long as Python 3.x is installed.

