f = open("./lotto.txt","r",encoding="utf-8")
total_data = f.readlines()
lotto = []
for i in range(0,5):
    single_data = total_data[i].strip().split(",")
    for j in range (0,len(single_data)):
        single_data[j] = int(single_data[j])
    lotto.append(single_data)
print(lotto)
#범위가 없는 경우.
#dic 사용.


count_list = {}

print(count_list)
for nums in lotto:
    for num in nums:
        count_list[num] = count_list.get(num, 0) + 1

print(count_list)

count_list_keys = count_list.keys()
a_max = 0
b_min = 0
for i in count_list_keys:
    if a_max< count_list.get(i):
        a_max = count_list.get(i)
    if b_min > count_list.get(i):
        a_min = count_list.get(i)

    count_list.get(i)
#범위가 있는 경우.
count_list = []
for i in range(0,45):
    count_list.append(0)

a = {}
print(max(list(count_list.values)))
print(count_list)
for nums in lotto:
    for num in nums:
        count_list[num-1] = count_list[num-1]+1

print(count_list)

max_num = max(count_list)
min_num = min(count_list)
max_nums = []
min_nums = []

for i in range(0,len(count_list)):
    if count_list[i] == max_num:
        max_nums.append(i+1)
    elif count_list[i] == min_num:
        min_nums.append(i+1)
f.close()

file = open("../csv_file/ana_lotto.txt","w",encoding="utf-8")

file.write(f"{max_nums},{max_num}")
file.write(f"{min_nums},{min_num}")

file.close()

# 처음에 파일에서 데이터를 받아온다.
# 내가 필요한 데이터만 뽑아 만든다.
# 카운트를 위해 필요범위로 카운트 리스트를 만든다.
# 필요한 데이터 내에서 카운트를 한다.
# 카운트 한 데이터에서 가장 많이 나온 수와 가장 적게 나온 수를 구한다.
# 데이터에 맞는 데이터 리스트를 만든다.
# 파일에 필요한 데이터를 형식맞게 작성하여 저장.
