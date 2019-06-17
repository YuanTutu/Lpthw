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

#print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age:{age},Height:{height},Weight:{weight},IQ:{iq}")


#A puzzle for the extra credit,type it in anyway.
#print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
#加减乘除四个依次嵌套进去，但是运算过程是反过来的

a = divide(iq,2)
b = multiply(weight,a)
c = subtract(height,b)
d = add(age,c)
#print("That becomes:",what,"Can you do it by hand?")
print("That becomes:",d,"Can you do it by hand?")
