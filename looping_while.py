def reverse():
    n = int(input("Enter the given value:"))
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    print(rev)

def strongnum():

    n = int(input(" Enter the Number:"))
    temp = n
    sum1 = 0
    count = 0
    while (n > 0):
        rem = n % 10
        fact = 1
        for i in range(rem, 0, -1):
            fact = fact * i
        n = n // 10
        sum1 = sum1 + fact
    if sum1 == temp:
        print(" The given number is a Strong Number")
    else:
        print("The given number is not a Strong Number")


def amstrongnum():
    n = int(input("Enter a number: "))
    sum1 = 0
    temp = n
    nd = 0
    while temp > 0:
        temp = temp // 10
        nd = nd + 1
    temp = n
    while temp > 0:
        digit = temp % 10
        sum1 = sum1 + digit ** nd
        temp //= 10
    if n == sum1:
        print(" It is a Armstrong number")
    else:
        print("It is not a Armstrong number")

def perfectnum():
    num = int(input("Enter the number:"))
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 = sum1 + i
    if sum1 == num:
        print("The given number is perfect number")
    else:
        print("The given number is not a perfect number")


def allprimenum():
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







