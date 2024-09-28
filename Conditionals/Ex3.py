# A leap year is a year that consists of 366 (not 365) days. 
# It occurs roughly every four years. More specifically, a 
# year is considered leap if it is either divisible by 4 but 
# not by 100 or it is divisible by 400.

year = int(input('Provide a year: '))
 
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')