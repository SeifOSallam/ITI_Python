def filterEvens(x):
    return x % 2 == 1

def squareList(x):
    return x*x
    
mylist = [1,2,3,4,5,6,7,8,9,10]

newlist = filter(filterEvens, mylist)

newlist = map(squareList, list(newlist))

print(list(newlist))