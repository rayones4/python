str=input("enter a string")
lower=""
upper=""
for var in str:
    if var.islower():
       lower=lower+var
    if var.isupper():
       upper=upper+var
new_str=lower + upper
new_str=lower + upper
print(new_str)