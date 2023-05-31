# Python program to display all the prime numbers within an interval


lower = int(inpt("enter lower bound"))
upper = int(input("enter upper bound"))

print("Prime numbers between",lower, upper, "are:")

for num in range(lower, upper + 1):

    if num >