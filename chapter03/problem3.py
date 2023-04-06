n, m = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(n)]
candidates = []

for num in numbers:
    candidates.append(min(num))

answer_num = max(candidates)

print(answer_num)