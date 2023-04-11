import time as times
n = int(input())

time_with_three = [3, 13, 23]
cnt = 0

start_time = times.time()
for time in range(0, n+1):
    if time in time_with_three:
        cnt += 3600
    else:
        cnt += 1575

end_time = times.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")