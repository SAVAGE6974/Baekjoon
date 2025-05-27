lines = [input() for _ in range(5)]

# 각 줄의 길이가 다를 수 있으므로 최대 길이를 기준으로 반복
max_len = max(len(line) for line in lines)

result = ""

# 열 우선 순회
for i in range(max_len):
    for line in lines:
        if i < len(line):  # 해당 열의 문자가 존재하는 경우만
            result += line[i]

print(result)
