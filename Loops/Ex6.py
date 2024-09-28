Weird = (5, 6, "Happy", False)

try:
    Weird[4] = "Sad"
except:
    print("You can not add elements to a tuple as it is immutable!")
