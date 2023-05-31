#convert elements of the list to uppercase and store in set
lst=['Abhinav','Abhiram','Ahan','Aishwarya','Ganesh']
lst1=[]
for var in lst:
    lst1.append(var.upper())
    print(set(lst1))