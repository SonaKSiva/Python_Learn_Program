import Variables
import selection
import looping_display
import looping_counting
import looping_series
import looping_while
import string
import list
import tuples
import set
import dictionary

def menudictionary():
    stat = True
    while (stat):
        print("1.Learning Dictionary")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            dictionary.learningdect()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False


def menuset():
    stat = True
    while (stat):
        print("1.Learning Set")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            set.learningset()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False


def menutuples():
    stat = True
    while (stat):
        print("1.Learning Tuples")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            tuples.learningtuples()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False

def menulist():
    stat = True
    while (stat):
        print("1.Learning List")
        print("2.Reading and displaying list elements")
        print("3.Copy array elements in reverse order")
        print("4.Find sum of all odd numbers in the given list")
        print("5.Search an element in the given list")
        print("6.Find the largest element in the given list")
        print("7.Find largest and smallest element in the given list")
        print("8.Read two list elements and compare them and display match found or not")
        print("9. Rotate list elements cyclically by one position")
        print("10. Delete an element at given position in the list")
        print("11.Insert an element at given position in the list")
        print("12.Find second largest element in the given list")
        print("13.Read and display two dimensional list")
        print("14.Matrix Addition")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            list.learnlist()
        elif ch == 2:
            list.readisp()
        elif ch == 3:
            list.cpyarrayele()
        elif ch == 4:
            list.alloddnum()
        elif ch == 5:
            list.searchele()
        elif ch == 6:
            list.largestele()
        elif ch == 7:
            list.largesmallele()
        elif ch == 8:
            list.compareele()
        elif ch == 9:
            list.cyclically()
        elif ch == 10:
            list.delele()
        elif ch == 11:
            list.insertele()
        elif ch == 12:
            list.seclargestele()
        elif ch == 13:
            list.twodimension()
        elif ch == 14:
            list.matrixadd()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False




def menustring():
    stat = True
    while (stat):
        print("1.Learning String")
        print("2.Find number of vowels in the given string")
        print("3.Find number of stopwords in the given string")
        print("4.Remove stopwords from the given string")
        print("5.Remove duplicate words in the given string")
        print("6.Find number of occurrences of each word in the given string")
        print("7. Find the least frequency character in the given string")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            string.learningstr()
        elif ch == 2:
            string.vowels()
        elif ch == 3:
            string.stopwords()
        elif ch == 4:
            string.remstopwords()
        elif ch == 5:
            string.remduplicate()
        elif ch == 6:
            string.occurword()
        elif ch == 7:
            string.leastfreq()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False
def menulooping_while():
    stat = True
    while (stat):
        print("1.Display the given number in reverse order")
        print("2.Find the given number is strong number or not")
        print("3. Find the given number is amstrong number or not")
        print("4.Find the given number is perfect number or not")
        print("5.Find sum of all prime numbers from n1 to n2")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            looping_while.reverse()
        elif ch == 2:
            looping_while.strongnum()
        elif ch == 3:
            looping_while.amstrongnum()
        elif ch == 4:
            looping_while.perfectnum()
        elif ch == 5:
            looping_while.allprimenum()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False


def menulooping_series():
    stat = True
    while (stat):
        print("1.Find sum of first n natural numbers")
        print("2.Find factorial of a number")
        print("3.Find sum of the series n**n+(n-1)**(n-1).......1")
        print("4.Find sum of the series n+ n**2+.....n**n")
        print("5.Find sum of prime numbers from n1 to n2")
        print("6.Display first n prime numbers")
        print("7.Find sum of the digits")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            looping_series.naturalnum()
        elif ch == 2:
            looping_series.factnum()
        elif ch == 3:
            looping_series.series()
        elif ch == 4:
            looping_series.sumseries()
        elif ch == 5:
            looping_series.sumprime()
        elif ch == 6:
            looping_series.firstprime()
        elif ch == 7:
            looping_series.sumdigit()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False

def menulooping_counting():
    stat = True
    while (stat):
        print("1.Find greatest of 2 numbers")
        print("2.Find how many divisors for the given number")
        print("3. Find the given number is prime or not")
        print("4. Find how many prime numbers from n1 to n2")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            looping_counting.greatestnumb()
        elif ch == 2:
            looping_counting.divisorsgn()
        elif ch == 3:
            looping_counting.gnprimeornot()
        elif ch == 4:
            looping_counting.primen1ton2()

        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont != 1:
            stat = False

def menulooping_display():
    stat = True
    while (stat):
        print("1.Display all even numbers from n1 to n2")
        print("2.Display all numbers divisible by n from n1 to n2")
        print("3.Display Multiplication table")
        print("4. Display all divisors of a given number")
        print("5. Display all prime numbers from n1 to n2")
        ch = int(int(input("Enter your choice: ")))
        if ch == 1:
            looping_display.evenn1ton2()
        elif ch == 2:
            looping_display.divisible()
        elif ch == 3:
            looping_display.multitable()
        elif ch == 4:
            looping_display.divisor()
        elif ch == 5:
            looping_display.primenum()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont!=1:
            stat = False

def menuselection():
    stat=True
    while(stat):
        print("1.Oddeven")
        print("2.Positive or Negative")
        print("3.Greatest of Two Number")
        print("4.Grade of the given mark")
        print("5.Display the give digit in Words")
        ch = int(int(input("Enter your choice: ")))
        if ch == 1:
            selection.oddeven()
        elif ch == 2:
            selection.posorneg()
        elif ch == 3:
            selection.greatestoftwo()
        elif ch == 4:
            selection.grade()
        elif ch == 5:
            selection.digitinwords()
        else:
            print("Invalid choice")
        cont=int(input("Press 1 to continue else to  exit variables menu"))
        if cont!= 1:
            stat=False


def menuvariable():
    stat = True
    while (stat):
        print("1.Addition")
        print("2.Expression")
        print("3.Convert the given number in meter to Centimeter")
        print("4.Area of Rectangle")
        print("5. Convert the given number in Celcius to Farenheit")
        ch = int(int(input("Enter your choice: ")))
        if ch == 1:
            Variables.addition()
        elif ch == 2:
            Variables.expression()
        elif ch == 3:
            Variables.centimeter()
        elif ch == 4:
            Variables.areaofrect()
        elif ch == 5:
            Variables.farenheit()
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to  exit variables menu"))
        if cont!=1:
           stat = False



stat = True
while(stat):
    print("1.Variables")
    print("2.Selection")
    print("3.Looping_display")
    print("4.Looping_counting")
    print("5.Looping_series")
    print("6.Looping_while")
    print("7.String")
    print("8.List")
    print("9.Tuples")
    print("10.Set")
    print("11.Dictionary")
    print("12.Functions")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        menuvariable()
    elif ch == 2:
        menuselection()
    elif ch == 3:
        menulooping_display()
    elif ch == 4:
        menulooping_counting()
    elif ch == 5:
        menulooping_series()
    elif ch == 6:
        menulooping_while()
    elif ch == 7:
        menustring()
    elif ch == 8:
        menulist()
    elif ch == 9:
        menutuples()
    elif ch == 10:
        menuset()
    elif ch == 11:
        menudictionary()
    elif ch == 12:
        menufunctions()
    else:
        print("Invalid choice")
    cont = int(input("Press 1 to continue else to exit project:"))
    if cont != 1:
        stat = False

