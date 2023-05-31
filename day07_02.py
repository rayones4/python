import math
def fun(n):
    return n*n
lst=[5,10,15,20,25]
m1=map(math.factorial,lst)
m2=map(fun, lst)
m3=map(lambda n:n ** 3, lst)

print(list(m1))
print(list(m2))
print(list(m3))