#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
def recurSum(n):
	if n <= 1:
		return n
	return n + recurSum(n - 1)

n = 10
print(recurSum(n))
