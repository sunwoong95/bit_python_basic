# a = [44,42,23,12,29,27,48,78,21,32]
# complete = []
# complete1 = []
# tmp1 = {}
# tmp2 = {}
# for y in range(0,len(a)):
#     if a[y]%2==0:
#         tmp1[y]=a[y]
#     else:
#          tmp2[y]=a[y]
# complete.append(tmp1)
# complete1.append(tmp2)


# print(complete)
# print(complete1)
# print(f"홀수는 {len(tmp2)}개 입니다.")


a =[["name","age","score"],
["park",11,100],
["kark",15,120],
["apark",1,110],
["bpark",19,100],
["lpark",12,100],
["qpark",5,1800]]

person_list = []
b = a[0]
c = a[1:]

for d in c:
    tmp={}
    for e in range(0,len(b)):
        tmp[b[e]] = d[e]
    person_list.append(tmp)
print(person_list)
d = 0
print(person_list[0]["score"])
for d in range(0,len(c)):
    if person_list[d]["score"]> 100:
        print("true")
    else:
        print("false")

from re import X


language_list = [{"name":"C","difficulty":6},{"name":"C++","difficulty":5},{"name":"Python","difficulty":3},{"name":"Java","difficulty":1},{"name":"Ruby","difficulty":10}]
# 각 프로그래밍 언어의 이름과 난이도를 반복문으로 분류하라.

x = language_list

for a in range(0,len(x)):
    print(f"프로그래밍 언어의 이름은 {x[a]['name']}입니다.")
    if x[a]['difficulty'] >5:
        print(f"표시된 난이도는 {x[a]['difficulty']}이며, 어려움 입니다.")
    elif 6 > x[a]['difficulty'] > 1:
        print(f"표시된 난이도는 {x[a]['difficulty']}이며, 보통 입니다.")
    else:
        print(f"표시된 난이도는 {x[a]['difficulty']}이며, 쉬움 입니다.")

