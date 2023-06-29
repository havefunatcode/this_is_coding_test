# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

n, m = map(int, input().split())
start_x, start_y, start_direction = map(int, input().split())
whole_map = [list(map(int, input().split())) for _ in range(n)]
whole_map[start_x][start_y] = 1
cnt = 0
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_x, current_y = start_x, start_y

def check_direction(start_direction: int, start_x: int, start_y: int) -> int:
    for i in range(4):
        start_direction -= 1
        if start_direction < 0:
            start_direction = 3

        moving_point = move[start_direction]
        tmp_x = moving_point[0] + start_x
        tmp_y = moving_point[1] + start_y

        if tmp_x >= n or tmp_y >= m or tmp_x < 0 or tmp_y < 0:
            return -1

        if whole_map[tmp_x][tmp_y] == 0:
            return start_direction

    return -1

current_direction = start_direction
while current_direction >= 0:
    current_direction = check_direction(current_direction, start_x, start_y)
    moving_point = move[current_direction]

    start_x += moving_point[0]
    start_y += moving_point[1]

    whole_map[start_x][start_y] = 1
    cnt += 1

    for row in whole_map:
        for element in row:
            if element == 0:
                continue


print(cnt)