def calc_fact(x):
    if x == 1:
        return 1
    
    if x == 0:
        return 1
    
    return x * calc_fact(x-1)

print(calc_fact(5))