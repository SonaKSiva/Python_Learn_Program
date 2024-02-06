def learnlist():
    mylist = [2, 3.6, "red", [6, 8]]

    mylist = [1, 4.5, "red", [5, 7]]
    print(mylist)
    print(len(mylist))
    print(type(mylist))

    # accessing list elements
    print(mylist[0])
    print(mylist[-1])
    print(mylist[1:3])

    # for loop

    for i in range(len(mylist)):
        print(mylist[i])

    for ele in mylist:
        print(ele)

    mylist.append(6)
    print(mylist)
    ele = [6, 8]
    if ele in mylist:
        print("Found")
    else:
        print("Not found")

    # Reading and displaying list

    n = 4
    list = []
    for i in range(n):
        list.append(int(input("Enter element value:")))
    print(list)


def readisp():
    n = int(input("Enter the n value:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element value:")))
    print(lis)
    for i in range(len(lis)):
        print(lis[i])
    for ele in lis:
        print(ele)

def cpyarrayele():
    mylist = [1, 2, 3, 4, 5];
    for i in range(len(mylist)):
        print(mylist[i])
    print("Array  element in reverse order: ");
    copy = []
    for i in range(len(mylist) - 1, -1, -1):
        copy.append(mylist[i])
    print(copy)

def alloddnum():
    mylist = [1, 2, 3, 4, 5]
    s = 0
    for i in mylist:
        if (i % 2 != 0):
            s = s + i
    print(s)

def searchele():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    se = int(input("Enter the search element:"))
    stat = 0
    for i in range(n):
        if lis[i] == se:
            stat = 1
    if stat == 1:
        print("Element is found")
    else:
        print("Element is not found")

def largestele():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    large = lis[0]
    for i in range(n):
        if lis[i] > large:
            large = lis[i]
    print(large)

def largesmallele():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    large = lis[0]
    for i in range(n):
        if lis[i] > large:
            large = lis[i]
    print("largest value is", large)
    small = lis[0]
    for i in range(n):
        if lis[i] < small:
            small = lis[i]
    print("smallest value is", small)

def compareele():
    n1 = int(input("Enter the number of elements:"))
    lis1 = []
    for i in range(n1):
        lis1.append(int(input("Enter element:")))
    print(lis1)
    n2 = int(input("Enter the number of elements:"))
    lis2 = []
    for i in range(n2):
        lis2.append(int(input("Enter element:")))
    print(lis2)
    stat = 0
    for i in range(n1):
        print(lis1[i])
        for j in range(n2):
            print(lis2[j])
            if lis1[i] == lis2[i]:
                stat = 1
    if stat == 0:
        print("match not found")
    else:
        print("match found")

def cyclically():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    temp = lis[-1]
    for i in range(n):
        temp1 = lis[i]
        lis[i] = temp
        temp = temp1
    print(lis)

def delele():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    pos = 2
    for i in range(n - 1):
        if i >= pos:
            lis[i] = lis[i + 1]
    lis.pop()
    print(lis)

def insertele():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    pos = 2
    ele = 20
    for i in range(n):
        if i == pos:
            temp = lis[i]
            lis[i] = ele
        elif i > pos:
            temp1 = lis[i]
            lis[i] = temp
            temp = temp1
    lis.append(temp)
    print(lis)

def seclargestele():
    n = int(input("Enter the number of elements:"))
    lis = []
    for i in range(n):
        lis.append(int(input("Enter element:")))
    print(lis)
    large = lis[0]
    for i in range(n):
        if lis[i] > large:
            large = lis[i]
    secondLarge = lis[0]
    for i in range(n):
        if lis[i] > secondLarge:
            if lis[i] != large:
                secondLarge = lis[i]
    print("Second Largest Number is:")
    print(secondLarge)



def twodimension():
    lis = []
    row = 3
    col = 3
    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(int(input("Enter the element:")))
        lis.append(temp)
    print(lis)
    for r in range(row):
        for c in range(col):
            print(lis[r][c])

def matrixadd():
    lis1 = []
    row = 3
    col = 2
    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(int(input("Enter the elements:")))
        lis1.append(temp)

    lis2 = []
    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(int(input("Enter the elementts:")))
        lis2.append(temp)

    lis3 = []
    for r in range(row):
        temp3 = []
        for c in range(col):
            temp3.append(lis1[r][c] + lis2[r][c])
        lis3.append(temp3)

    print(lis1)
    print(lis2)
    print(lis3)








































