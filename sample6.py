#max in list
lst=[]
n=int(input("enter number of elements"))
print("enter elements of the list")
for i in range(n):
    ele=int(input())
    lst.append(ele)
print("Largest element in the list is",max(lst))