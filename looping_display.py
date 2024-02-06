def evenn1ton2():
    n1 = int(input("Enter the n1 number:"))
    n2 = int(input("Enter the n2 number:"))
    for i in range(n1, n2):
        if i % 2 == 0:
            print(i, end=" ")

def divisible():
    n1 = int(input("Enter the n1 number:"))
    n2 = int(input("Enter the n2 number:"))
    n = int(input("Enter the divisible number:"))
    for i in range(n1, n2):
        if i % n == 0:
            print(i, end=" ")

def multitable():
    tableno = int(input("Enter the tableno:"))
    upperlimit = int(input("Enter the upperlimit:"))
    for i in range(1, upperlimit + 1):
        print(tableno, "x", i, "=", tableno * i)


def divisor():
    n = 25
    upperlimit = 25
    for i in range(1, upperlimit + 1):
        if n % i == 0:
            print(i)

def primenum():
    n1 = int(input("Enter the n1 number:"))
    n2 = int(input("Enter the n2 number:"))
    for i in range(n1, n2):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            print(i)



