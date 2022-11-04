a = [
[3, 23, 85, 34, 17, 74, 25, 52, 65] ,
[10, 7, 39, 42, 88, 52, 14, 72, 63] ,
[87, 42, 18, 78, 53, 45, 18, 84, 53],
[34, 28, 64, 85, 12, 16, 75, 36, 55],
[21, 77, 45, 35, 28, 75, 90, 76, 1],
[25, 87, 65, 15, 28, 11, 37, 28, 74],
[65, 27, 75, 41, 7, 89, 78, 64, 39],
[47, 47, 70, 45, 23, 65, 3, 41, 44],
[87, 13, 82, 38, 31, 12, 29, 29, 80]
]

# 각행 소수 개수  4
# 최대값이 각행 몇열에 있는지	3
# 최소값이 각행 몇열에 있는지	1
# 열에 합으로 가장 큰 열 과 그 수	2
# 각행 소수 개수  4
# 1. 하나부터 소수 
# 2. 리스트에서 소수 개수 구하기
# 3. 많은 리스트에서 각각 소수 개수 구하기 

b= []
for i in range(0,len(a)):
    b = a[i] 
    max_b = max(b)
    for j in range(0,len(b)):
        if max_b == b[j]:
            print(f"{i+1}열의 최댓값은 {max_b}이며, {j+1}번째에 위치합니다.")

b= []
for i in range(0,len(a)):
    b = a[i] 
    min_b = min(b)
    for j in range(0,len(b)):
        if min_b == b[j]:
            print(f"{i+1}열의 최솟값은 {min_b}이며, {j+1}번째에 위치합니다.")

b = []

for i in range(0,len(a)):
    x = a[i]
    z = 0
    for y in range(0,len(x)):
        z = z + x[y]
    b.append(z)

b = []

x,y = 0, 0

while x < len(b):
    if y < b[x]:
        y = b[x]
        x = x + 1
    else:
        x = x + 1

c = b.copy()
c.sort()
c.reverse()

for i in range(0,len(b)):
    if c[0] == b[i]:
        print(f"열의 합이 가장 큰 열은 {i+1}열 입니다.")
        print(f"{i+1}열{a[i]}의 합은 {b[i]}입니다.")

b_max = max(b)

for i in range(0,len(b)):
    if b_max == b[i]:
        print(f"열의 합이 가장 큰 열은 {i+1}열 입니다.")
        print(f"{i+1}열{a[i]}의 합은 {b[i]}입니다.")

for i in range(0,len(b)):
    if y == b[i]:
        print(f"열의 합이 가장 큰 열은 {i+1}열 입니다.")
        print(f"{i+1}열{a[i]}의 합은 {b[i]}입니다.")        