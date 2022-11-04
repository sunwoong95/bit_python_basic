f = open("./../csv_file/9898.csv","r",encoding="utf-8")
total_data = f.readlines()
data_keys = total_data[0].strip().split(",")
data_list = []

for i in range(1,len(total_data)):
    data1 = total_data[i].strip().split(",")
    dict1 = {}
    for j in range(0, len(data1)):
        dict1[data_keys[j]] = data1[j]
    data_list.append(dict1)

total_price = 0
avg_person_list = []
name_list = []

for i in range(0,len(data_list)):
    total_price += int(data_list[i].get("price"))

price_avg = total_price/len(data_list)

for i in range(0,len(data_list)):
    if int(data_list[i].get("price")) > price_avg:
        avg_person_list.append(data_list[i])
        name_list.append(data_list[i].get("name"))

print(avg_person_list)

print(f"인원수 : {len(avg_person_list)}")
for i in range(0,len(name_list)):
    print(f"고객명 : {name_list[i]}")


f.close()



