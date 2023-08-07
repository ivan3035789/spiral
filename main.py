input_value = int(input())
nul = [[0] * input_value for i in range(input_value)]
x, y = 0, 0
for i in range(1, input_value ** 2 + 1):
    nul[x][y] = i
    if x <= y+1 and x+y < input_value-1:
        y += 1
    elif x < y:
        x += 1
    elif x+y >= input_value:
        y -= 1
    elif x >= y:
        x -= 1
for i in range(input_value):
    print(*nul[i])