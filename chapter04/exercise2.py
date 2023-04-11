n = int(input())

cnt = 0

for time in range(0, n + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in str(second) or '3' in str(minute) or '3' in str(time):
                cnt += 1

print(cnt)