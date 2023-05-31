squares = {x: x*x for x in range(12) if x%2==0}
print(squares)
for i in squares:
    print(squares[i])
    print(6 in squares)
    print(6 not in squares)