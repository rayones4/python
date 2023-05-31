#string Palindrome
#madam
str=input("enter a string")
rev=str[::-1]
if str==rev:
    print(str, "is a palindrome")
else:
    print(str,"is not a palindrome")