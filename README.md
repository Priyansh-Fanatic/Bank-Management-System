## Table of contents
* [General info](#general-info)
* [Demo](#demo)
* [Features](Features)
* [Installation](Installation)
    
## General info

The Bank Management System is a Python-based desktop application designed to simulate basic banking operations. Built using the **Tkinter** library for the graphical user interface (GUI) and **MySQL** for database management, this application provides a user-friendly platform for users to manage their bank accounts. It includes features for user registration, login, balance management, money transfers, and transaction history tracking.


## Demo


- ### **To create or log into an account.**
    



https://github.com/user-attachments/assets/3a09ec55-83e3-43a1-aa17-e5ba31d8710b


- ### **Functions of the application.**


https://github.com/user-attachments/assets/74d1abd1-9cab-42dc-a5ff-e5180e50db3b






## Features

__1. User Authentication:__

- __Login:__ Users can log in with their username and password. Proper validation and error handling ensure security and ease of use.
- __Sign Up:__ New users can create an account by providing a username, password, name, and pin. Each new account is assigned a unique account number, and the user’s initial balance is set to zero.
__2. Home Page:__

- Upon successful login, users are directed to the home page, where they can view their account details, including the account holder's name, account number, and current balance.
- Options to log out, add money, withdraw money, transfer money, and view transaction history are available.
__3. Account Management:__

- __Add Money:__ Users can add money to their account. The application ensures the amount is positive and updates the balance accordingly.
- __Withdraw Money:__ Users can withdraw money from their account. The system checks for sufficient balance before processing the withdrawal.
- __Transfer Money:__ Users can transfer money to another account within the same system by entering the recipient’s account number and the transfer amount. The system validates the recipient’s account number and ensures the user has sufficient funds.
__4. Transaction History:__

- Users can view their transaction history, which includes details such as the transaction date, amount, description, and balance after each transaction. The history is displayed in a scrollable window for ease of navigation.
__5. Database Management:__

- The system uses MySQL for database operations. Tables are created and managed to store user information and transaction records.
- On first run, the system checks for the existence of the necessary database and tables, creating them if they do not exist.


## Installation

- Clone the project

```bash
  git clone https://github.com/Priyansh-Fanatic/Bank-Management-System.git
```

- Once the repository is cloned, navigate into the project directory

```bash
  cd Bank-Management-System
```
__You can now start working with the files in the repository.__

## Author

- **[Priyansh](https://github.com/Priyansh-Fanatic)**

