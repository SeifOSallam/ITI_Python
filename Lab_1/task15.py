def operations(mylist):
    sum = 0
    min = mylist[0]
    max = mylist[0]
    squaredlist = []
    for i in mylist:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
        squaredlist.append(i*i)
    
    print('sum = ' + str(sum))
    print('min = ' + str(min))
    print('max = ' + str(max))
    return squaredlist

print(operations([1,2,3,4,5]))