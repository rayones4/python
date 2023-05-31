# iterate the first 10 numbers and in each iteration, print sum of current and previous number
#1: sum 0 + 1 =1
#2: sum 1 + 2 = 3
prev=0
for i in range(1,11):
    curr=i
    sum=prev + curr
    print("sum of {0} and {1} is {2}".format(prev,curr,sum))
    prev=curr