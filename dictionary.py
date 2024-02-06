def learningdect():
    # Defining Dictionary key:value
    mydict = {
        "name": ["Raja", "Arun"],
        "age": [20, 19],
        "color": "red"
    }
    print(mydict)
    print(len(mydict))
    print(type(mydict))

    # accessing Dictionary
    print(mydict["name"])
    print(type(mydict["name"]))
    print(type(mydict["color"]))
    print(mydict.keys())

    # Add
    mydict["fruit"] = ["orange", "apple"]
    print(mydict)
    # update
    mydict["color"] = "blue"
    print(mydict)

    mydict.update({"color": "yellow"})
    print(mydict)

    print("**" * 20)
    for x in mydict:
        print(x)
        print(mydict[x])

    print("##" * 20)
    for x in mydict.values():
        print(x)

    for x in mydict.keys():
        print(x)

    for x, y in mydict.items():
        print(x, y)

    mydict1 = mydict.copy()
    print(mydict1)

    # removing
    mydict.pop("age")
    print(mydict)

    mydict.popitem()
    print(mydict)

    # del mydict
    # print(mydict)
    # mydict.clear()
    print(mydict)

    # Nested Dictionary

    myclassstudents = {
        "child1":
            {
                "name": "Arun",
                "assignmnet": [50, 60, 0],
                "classtest": [45, 67]
            },
        "child2":
            {
                "name": "Arun",
                "assignmnet": [50, 60, 0],
                "classtest": [45, 67]
            }

    }

    print(myclassstudents)
