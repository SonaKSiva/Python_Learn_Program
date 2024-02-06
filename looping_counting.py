def greatestnumb():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    if a > b:
        print(a, "is greatest number")
    elif a < b:
        print(b, "is greatest number")
    else:
        print(" Both are equal")



def divisorsgn():
    n = int(input("Enter the value:"))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    print(count)

def gnprimeornot():
    n = int(input("Enter the value:"))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print("The given number is prime number")
    else:
        print("The given number is not a prime number")

def primen1ton2():
    n1 = int(input("Enter the n1 value:"))
    n2 = int(input("Enter the n2 value:"))
    counter = 0
    for i in range(n1, n2):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            counter = counter + 1
    print(counter)





