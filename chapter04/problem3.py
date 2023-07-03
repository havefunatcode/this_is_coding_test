# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1
whole_map = [list(map(int, input().split())) for _ in range(n)]
x_degree = [-1, 0, 1, 0]
y_degree = [0, 1, 0, -1 ]

def find_direction() -> int:
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    find_direction()
    current_x = x + x_degree[direction]
    current_y = y + y_degree[direction]

    if whole_map[current_x][current_y] == 0 and d[current_x][current_y] == 0:
        d[current_x][current_y] = 1
        x = current_x
        y = current_y
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        current_x = x - x_degree[direction]
        current_y = y - y_degree[direction]

        if whole_map[current_x][current_y] == 0:
            x = current_x
            y = current_y
        else:
            break
        turn_time = 0

print(count)