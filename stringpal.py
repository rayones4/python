#Count the total number of digits in a number
#1326 = 12 - sum of digits
#1326 = 4 - count of digits
num=int(input("ENTER A NUMBER"))
temp=num
sum=0
count=0
while num!=0:
    d=num%10
    sum=sum+d
    num=num//10
    count=count+1
print("sum of the digits in {0} is {1}".format(temp,sum))
print("Number of digits in {0} is {1}".format(temp,count))
