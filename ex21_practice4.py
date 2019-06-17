def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

a = 24
b = 34
c = 100
d = 1023

divide = divide(b,c)
add = add(a,divide)
subtract = subtract(add,d)

print(subtract)
