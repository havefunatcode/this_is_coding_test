start_position = list(str(input()))
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
column = columns.index(start_position[0]) + 1
row = int(start_position[1])

knight_moving_process_one = [(+2, +1), (+2, -1), (-2, +1), (-2, -1)]
knight_moving_process_two = [(+1, +2), (-1, +2), (+1, -2), (-1, +2)]
count = 0

for dx, dy in knight_moving_process_one:
    tmp_x = column + dx
    tmp_y = row + dy
    if tmp_x < 1 or tmp_y < 1 or tmp_x >= 8 or tmp_y > 8:
        continue
    count += 1

for dx, dy in knight_moving_process_two:
    tmp_x = column + dx
    tmp_y = row + dy
    if tmp_x < 1 or tmp_y < 1 or tmp_x >= 8 or tmp_y > 8:
        continue
    count += 1

print(count)