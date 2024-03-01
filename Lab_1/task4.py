def square_list(list):
    newlist = []
    for i in list:
        newlist.append(i*i)
    return newlist

print(square_list([2,3,4,5]))