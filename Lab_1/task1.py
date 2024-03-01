try :
    num = int(input("Please enter a number\n"))
    if num >= 20 and num <= 50:
        print('Within range')
    else:
        print('Out of range')
except:
    print('Enter a valid number')