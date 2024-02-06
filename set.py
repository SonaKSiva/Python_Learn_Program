def learningset():
    myset = {1, 2, 3, 6, 3, 5, 7}
    print(myset)
    print(type(myset))

    # accessing elements
    for elements in myset:
        print(elements)

    print(6 in myset)
    myset.add(22)
    print(myset)

    # update
    myset1 = {22, 33, 55}
    myset.update(myset1)
    print(myset)

    myset.remove(33)
    print(myset)

    myset.discard(7)
    print(myset)

    myset.add("Raja")
    print(myset)

    ele = myset.pop()
    print(ele)
    ele = myset.pop()
    print(ele)
    print(myset)

    # set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.symmetric_difference(set2))


