import re

n = int(input())

for i in range(n):
    mobile_num = input()
    pattern = r"^[789]\d{9}$"
    match = re.match(pattern, mobile_num)
    if match:
        print("YES")
    else:
        print("NO")
