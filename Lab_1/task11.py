def palindrom(str):
    rev = str[::-1]
    if str == rev:
        print('Palindrom')
    else:
        print('Not Palindrom')


palindrom('Hello')

palindrom('eezee')