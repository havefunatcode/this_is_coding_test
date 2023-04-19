start_position = input()
column = int(ord(start_position[0])) - int(ord('a')) + 1
row = int(start_position[1])

knight_moving_process = [(+2, +1), (+2, -1), (-2, +1), (-2, -1), (+1, +2), (-1, +2), (+1, -2), (-1, +2)]
count = 0

for dx, dy in knight_moving_process:
    tmp_x = column + dx
    tmp_y = row + dy
    if tmp_x >= 1 and tmp_y >= 1 and tmp_x <= 8 and tmp_y <= 8:
        count += 1

print(count)