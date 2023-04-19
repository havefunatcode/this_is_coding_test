start_position = input()
row = int(start_position[1])
column = int(ord(start_position[0])) - int(ord('a')) + 1

steps = [(+2, +1), (+2, -1), (-2, +1), (-2, -1), (+1, +2), (-1, +2), (+1, -2), (-1, +2)]

count = 0
for dx, dy in steps:
    nx = row + dx
    ny = column + dy
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)