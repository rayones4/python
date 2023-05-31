str="I am 20 years studying in 2nd year"
sub=""
for var in str:
    if var.isdigit():
        sub=sub + var
print(sub)