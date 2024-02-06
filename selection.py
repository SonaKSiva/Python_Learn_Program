def oddeven():
    a = int(input("Enter a number to check odd or even:"))
    if a % 2 == 0:
        print(a, "is even number")
    else:
        print(a, "is odd number")


def posorneg():
    a = int(input("Enter the given number is positive or negative:"))
    if a > 0:
        print(a, "is positive")
    elif a < 0:
        print(a, "is negative")
    else:
        print(a, "is neither positive nor negative")

def greatestoftwo():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    if a > b:
        print(a, "is greatest number")
    elif a < b:
        print(b, "is greatest number")
    else:
        print(" Both are equal")


def grade():
    a = int(input("Enter the mark:"))
    if a > 100:
        print("Invalid")
    elif a > 75:
        print("Distinction")
    elif a > 60:
        print("First class")
    elif a > 45:
        print("Second class")
    elif a >= 0:
        print("Fail")
    else:
        print("Invalid")

def digitinwords():
    a = int(input("Enter the number:"))
    if a == 0:
        print("Zero")
    elif a == 1:
        print("One")
    elif a == 2:
        print("Two")
    elif a == 3:
        print("Three")
    elif a == 4:
        print("Four")
    elif a == 5:
        print("Five")
    elif a == 6:
        print("Six")
    elif a == 7:
        print("Seven")
    elif a == 8:
        print("Eight")
    elif a == 9:
        print("Nine")
    else:
        print("Invalid")

