def createmenu():
    stat = True
    while (stat):
        print("1.Addition")
        print("2.Greatest")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            print("Addition")
        elif ch == 2:
            print("Greatest")
        else:
            print("Invalid choice")
        cont = int(input("Press 1 to continue else to return:"))
        if cont != 1:
            stat = False

def nanr():
    def add():
        a = int(input("Enter the value for a:"))
        b = int(input("Enter the value for b:"))
        ans = a + b
        print(ans)

    add()

def add_wawr(x,y):
    res = x+y
    return res
a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
ans = add_wawr(a,b)
print(ans)


def add_wanr(x,y):
    res=x+y
    print(res)
a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
add_wanr(a,b)


def add_nawr():
    x = int(input("Enter the vaalue for x:"))
    y = int(input("Enter the value for y:"))
    res = x + y
    return res


ans = add_nawr()
print(ans)












