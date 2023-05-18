import warnings
import logging
from datetime import datetime

logging.basicConfig(filename="logs.txt", level=20, filemode='w', format='%(name)s - %(message)s')

def loginAdmin(function):
    def checkLogin(*args, **kwargs):
        login = args[0]
        if login == "ADMIN":
            return function(args)
        else:
            warnings.warn("This is method only for admin")
    return checkLogin

def loginUser(function):
    def checkLogin(*args, **kwargs):
        login = args[0]
        if not login == "ADMIN":
            print("here")
            logging.log(20, f"{datetime.now()}: Użytkownik {login} wywołał metodę {function.__name__}")
            return function(args)
        else:
            return function(args)
    return checkLogin

@loginAdmin
def doWhenAdmin(login):
    print("Now you are doing actions as admin")

@loginUser
def doWhenUser(login):
    print("Now you are doing actions as user")
