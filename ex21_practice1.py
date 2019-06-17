def test(a,b,c):
    print(f"{a}-{b}+{c}")
    return a-b+c

result1 = test(5,1,3)

print(f"it is {result1}.")

def test_1(e,f):
    print(f"{e}*{f}")
    return e*f

number_1 = int(input("No.1 is>>>"))
number_2 = int(input("No.2 is>>>"))

result2 = test_1(number_1,number_2)
print(f"the result of test_1 is {result2} ")
