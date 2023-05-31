i=1
while i<=3:
    p=float(input("enter principal amount"))
    t=int(input("enter number of years"))
    r=float(input("enter rate of interest"))
    si=p * t* r/100
    print("Simple interest =Rs.",si)
    i=i+1
