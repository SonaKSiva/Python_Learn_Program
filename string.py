def learningstr():
    mystring = "Hard work never fails"
    print(mystring)
    print(type(mystring))
    print(len(mystring))

    # accessing character
    print(mystring[0])  # print from first
    print(mystring[1])
    print(mystring[-1])  # print from last
    print(mystring[5:9])
    print(mystring[:9])
    print(mystring[5:])

    # Accessing character using loop
    for character in mystring:
        print(character, end="")

    print("")

    for i in range(len(mystring)):
        print(mystring[i], end=" ")

    print("")

    for word in mystring.split():
        print(word, end=" ")

    print("")

    print(mystring.upper())
    print(mystring.lower())
    print(mystring.count('Ha'))


def vowels():
    mystring = "Hard work never fail"
    vowels = 'aeiouAEIOU'
    s = 0
    for vowel in vowels:
        count = mystring.count(vowel)
        s = s + count
    print(s)

def stopwords():
    mystring = "Find number of stopword in the given string"
    stopwords = "the and it for but my your our in"
    s = 0
    for stopword in stopwords.split():
        count = mystring.count(stopword)
        print(stopword, mystring.count(stopword))
        s = s + count
    print(s)


def remstopwords():
    mystring = "Remove stopword in the given string"
    stopwords = "the and it for but my your our in"
    newstring = ''
    for word in mystring.split():
        if word not in stopwords.split():
            newstring = newstring + word + " "
    print(newstring)



def remduplicate():
    mystring = "Remove the duplicate words in the given string"
    newstring = ''
    for word in mystring.split():
        if word not in newstring.split():
            newstring = newstring + word + " "
    print(newstring)



def occurword():
    mystring = "Remove the duplicate words in the given string words"
    newstring = ''
    for word in mystring.split():
        if word not in newstring.split():
            newstring = newstring + word + " "
    print(newstring)
    for word in newstring.split():
        count = mystring.count(word)
        print(word, "-", count)

def leastfreq():
    mystring = "Enter the least frequency character in the given string"
    newstring = ''
    for character in mystring:
        if character not in newstring:
            newstring = newstring + character + ""
    print(newstring)
    for character in newstring:
        count = mystring.count(character)
        print(character, "-", count)





















