def sum_prod(x,y,z):
    ss=x+y+z
    pp=x*y*z
    return ss, pp
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
s,p = sum_prod(a,b,c)
print(s,p)