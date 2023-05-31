day = int(input("enter a day"))
if(day % 30 == 0) and (day % 10 == 0):
    print("{0} is a sex having day".format(day))
elif(day % 3 ==0) and (day % 10 != 0):
    print("{0} is a sex having day".format(day))
else:
    print("{0} is not a sex having day".format(day))
