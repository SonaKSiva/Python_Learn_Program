def naturalnum():
    n = int(input("Enter the value:"))
    sum1 = 0
    for i in range(1, n + 1):
        sum1 = sum1 + i
    print(sum1)

def factnum():
    num = int(input("Enter a number: "))
    factorial = 1
    if num > 0:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)

def series():
    n = int(input("Enter the number of terms: "))
    sum1 = 0
    for i in range(n):
        sum1 = sum1 + (n - i) ** (n - i)
    print("the sum of series is", sum1)

def sumseries():
    n = int(input("Enter the number of terms: "))
    sum1 = 0
    for i in range(1, n + 1):
        sum1 = sum1 + n ** 2 + n ** n
    print("the sum of series is", sum1)

def sumprime():
    n1 = int(input("Enter the n1 number:"))
    n2 = int(input("Enter the n2 number:"))
    sum1 = 0
    for i in range(n1, n2):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c = c + 1
        if c == 2:
            sum1 = sum1 + i
    print(sum1)


def firstprime():
    n = int(input("Enter the number for n:"))
    count = 0
    i = 1
    while count < n:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c = c + 1
        if c == 2:
            print(i)
            count = count + 1
        i = i + 1

def sumdigit():
    n = int(input("Enter the given number:"))
    temp = n
    count = 0
    while n > 0:
        rem = n % 10
        count = count + rem
        n = n // 10
    print(count)










