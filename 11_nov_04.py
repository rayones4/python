#remove aall the characters except integers
import re
str="I am 20 years old. I am  in my 2nd year BE"
op="202"
pattern='\d+'
sub=re.findall(pattern,str)
print(sub)
substr=""
for var in sub:
    substr=substr + var
print(substr)