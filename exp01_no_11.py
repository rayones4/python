lst=[]
n=int(input("How many elements in the list?"))
print("enter the elements of the list")
for i in range(n):
    ele=input()
    lst.append(ele)
lst1=[]
for var in lst:
    lst1.append(var.upper())
print(set(lst1))