import re
str= input("enter text")
sub=input("enter a sub string in the given text")
string=str.lower()
pattern=sub.lower()
count=re.findall(pattern,string)
print(len(count))