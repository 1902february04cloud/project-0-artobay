import json

dbname = 'db.json'

initial_db = {
    "users": {}
}


def dbwrite(db):
    global dbname
    with open(dbname, 'w') as fp:
        json.dump(db, fp)

def dbread():
    global dbname
    with open(dbname, 'r') as fp:
        db = json.load(fp)
        return db


def findUserByName(name):
    db = dbread()
    try:
        foundUser = db["users"][name]
        return foundUser
    except KeyError:
        return None

def insertUser(name, password):
    db = dbread()
    db["users"][name] = {
        "name": name,
        "password": password, 
        "balance": 0, 
        "transactions": []
    }
    dbwrite(db)
    return 

def findUserBalance(name):
    db = dbread()
    return db["users"][name]["balance"]

def addToUserBalance(name, amount):
    db = dbread()
    db["users"][name]["balance"] += amount
    dbwrite(db)
    return db["users"][name]["balance"]

def subtractFromUserBalance(name, amount):
    db = dbread()
    db["users"][name]["balance"] -= amount
    dbwrite(db)
    return db["users"][name]["balance"]

def addNewTransaction(name, type, amount):
    db = dbread()
    db["users"][name]["transactions"].append("{} {}$".format(type, amount))
    dbwrite(db)

def getAllTransactions(name):
    db = dbread()
    return db["users"][name]["transactions"]