import datetime

def greet(name):
    """This function greets someone by name"""
    message = f"Hello, {name}!"
    x = datetime.datetime.now()
    message += " Happy " + x.strftime("%A")

    return message


name = "Thurston"
greet_message = greet(name)

print(greet_message)

