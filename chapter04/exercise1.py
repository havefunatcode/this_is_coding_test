n = int(input())
plans = map(str, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
destination = ['L', 'R', 'U', 'D']
cx = 1
cy = 1

for plan in plans:
    cur_destination = destination.index(plan)
    tmp_x = cx + dx[cur_destination]
    tmp_y = cy + dy[cur_destination]
    if tmp_x == 0 or tmp_y == 0:
        continue

    cx = tmp_x
    cy = tmp_y

print(f"{cx} {cy}")