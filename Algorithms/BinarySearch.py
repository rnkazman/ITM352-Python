searchMe  = [ 2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

target = 0
while target != -1:
    try:
        target = int(input("Enter a number to search for: "))
        result = binary_search(searchMe, target)
        if result is not None:
            print(f"Found {target} at index {result}")
        else:
            if target != -1:
                print(f"{target} not found in the list")
    except ValueError:
        print("Please enter a valid integer.")
