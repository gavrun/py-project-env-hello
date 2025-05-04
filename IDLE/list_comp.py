l = [x**2 for x in range(4)]
print(l)
# [0, 1, 4, 9]

squares = {x**2 for x in [0,2,4] if x < 4}
print(squares)
# {0, 4}
