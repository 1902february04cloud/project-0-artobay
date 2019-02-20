from model.db import findUserByName, insertUser, findUserBalance, addToUserBalance, subtractFromUserBalance, addNewTransaction, getAllTransactions
from error.UserNotFoundError import UserNotFoundError


current_user = '' 

def show_help():
    print('1. help')
    print('2. register <name> <password>')
    print('3. login <name> <password>')
    print('4. balance')
    print('5. deposit <amount>')
    print('6. withdraw <amount>')
    print('7. transactions')
    print('8. logout')

def register(name, password):
    global current_user
    foundUser = findUserByName(name)
    if not foundUser:
        insertUser(name, password)
        current_user = name
        return "user successfully registered"
    else:
        return "A user with this name already exists."

def login(name, password):
    global current_user
    foundUser = findUserByName(name)
    if foundUser:
        current_user = name
        return "user successfully logged in"
    else:
        raise UserNotFoundError()

def logout():
    global current_user
    current_user = ''
    return "user successfully logged out"

def balance():
    global current_user
    if current_user == '':
        return 'User not logged in'
    return findUserBalance(current_user)

def deposit(amount):
    global current_user
    if current_user == '':
        return 'User not logged in'
    amount = int(amount)
    newBalance = addToUserBalance(current_user, amount)
    addNewTransaction(current_user, 'deposit', amount)
    return "deposit successful, new balance is: {}".format(newBalance)

def withdraw(amount):
    global current_user
    if current_user == '':
        return 'User not logged in'
    amount = int(amount)
    if findUserBalance(current_user) > amount:
        newBalance = subtractFromUserBalance(current_user, amount)
        addNewTransaction(current_user, 'withdraw', amount)
        return "withdraw successful, new balance is: {}".format(newBalance)
    else:
        return "Low Balance."

def transactions():
    global current_user
    if current_user == '':
        return 'User not logged in'
    transactions = getAllTransactions(current_user)
    return "\n".join(transactions)


def read_input(params):
    if params[0] == 'help':
        show_help()
    elif params[0] == 'register':
        if len(params) != 3:
            return "Usage: register <name> <password>"
        return register(params[1], params[2])
    elif params[0] == 'login':
        if len(params) != 3:
            return "Usage: login <name> <password>"
        return login(params[1], params[2])
    elif params[0] == 'logout':
        if len(params) != 1:
            return "Usage: logout"
        return logout()
    elif params[0] == 'balance':
        if len(params) != 1:
            return "Usage: balance"
        return balance()
    elif params[0] == 'deposit':
        if len(params) != 2:
            return "Usage: deposit <amount>"
        return deposit(params[1])
    elif params[0] == 'withdraw':
        if len(params) != 2:
            return "Usage: withdraw <amount>"
        return withdraw(params[1])
    elif params[0] == 'transactions':
        if len(params) != 1:
            return "Usage: transactions"
        return transactions()
    return ""