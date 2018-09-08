a = 'anu'  #global variable
b = 99     #global variable
print(f'{a} has a value of {b}')

print(a+str(b))


def somefunct():
    f = 55  #local variable
    global a, b
    print(a,b)
    print(f)


somefunct()


