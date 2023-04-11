n = int(input())

time_with_three = [3, 13, 23]
cnt = 0

for time in range(0, n+1):
    if time in time_with_three:
        cnt += 3600
    else:
        cnt += 1575

print(cnt)