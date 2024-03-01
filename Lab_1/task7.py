def check_keys(dict):
    if (dict.get('job') == None) and (dict.get('card_number') == None):
        print("doesn't have keys")
    else:
        print('has keys')

check_keys({
    "name": "jone", 
    "email": "jane@outlook.com", 
    "age": 25,
    "job": "engineer", 
    "address": "cairo, Egypt"
})

check_keys({
    "name": "jone", 
    "email": "jane@outlook.com", 
    "age": 25,
    "job": "engineer",
    "card_number": 1,
    "address": "cairo, Egypt"
})