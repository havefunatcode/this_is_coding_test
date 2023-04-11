import time as times
n = int(input())

cnt = 0

start_time = times.time()
for time in range(0, n + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in str(second) or '3' in str(minute) or '3' in str(time):
                cnt += 1

end_time = times.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")