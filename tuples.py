def learningtuples():
    mytuple = (1, "red", 55, 23.67)
    print(mytuple)
    print(type(mytuple))
    print(len(mytuple))

    # access elements
    print(mytuple[0])
    print(mytuple[-1])
    print(mytuple[2:])
    print(mytuple[:2])
    print(mytuple[:-2])

    element = "Red"
    if element.lower() in mytuple:
        print("found")
    else:
        print("not found")

    # updating
    mylist = list(mytuple)
    print(mylist)
    mylist.append("Raja")
    mylist[1] = "green"
    mytuple = tuple(mylist)
    print(mytuple)

    # unpacking
    (*a, b, c) = mytuple
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(c)
    print(type(c))
