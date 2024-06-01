squares=[]

for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)
squares.clear()

for value in range(1,11):
    squares.append(value**2)

print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))