myList = [1,2,"a", (1,2,3), True, [3,2,"b"],11,1,1,1,1]
listOfLists = [[1]*10, [2]*3, [3]*7, [4]*15]
num = int(input("Enter a number between 0 and 3: "))

while (num >=0 and num <=3):
    listLen = len(listOfLists[num])
    theList = listOfLists[num]

    if(listLen < 5):
        print(f"The list {theList} has fewer than 5 elements")
    elif( 5 <= listLen <= 10):
        print(f"The list {theList} has at least 5 but at most 10 elements")
    else:
        print(f"The list {theList} has more than 10 elements")
    num = int(input("Enter a number between 0 and 3: "))
    
    

