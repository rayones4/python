str="python"
new_string=str[0]
l=len(str)
new_string=new_string + str[l//2]
new_string=new_string + str[l-1]
print("New string is",new_string)