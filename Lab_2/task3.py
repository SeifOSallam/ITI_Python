import math
import json

numbers = [4, 9, 16, 25, 36]

sqrt_nums = map(lambda x: math.sqrt(x), numbers)

dict = {
    "nums" : numbers,
    "square root" : list(sqrt_nums)
}

file = open('dictionary.json' , 'w')

json.dump(dict, file)

file.close()