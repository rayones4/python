c=1# global variable

def add():
    global c
    c = c +3
    print("inside function",c)

add()
print("outside function",c)