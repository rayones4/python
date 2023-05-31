# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)
odd.extend([9, 11, 13])

print(odd)

print(odd + [9, 7, 5])
print(odd)
print(odd.pop())
print(odd)
print(odd.pop(3))
print(odd)
print(odd.remove(9)) # element the you want to delete
print(odd)


print(["re"] * 3)