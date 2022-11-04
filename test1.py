f = open("./../csv_file/person.csv","r",encoding="utf-8")
total_data = f.readlines()
data_keys = total_data[0].strip().split(",")
data_list = []
for i in range(1,len(total_data)):
    data1 = total_data[i].strip().split(",")
    dict1 = {}
    for j in range(0, len(data1)):
        dict1[data_keys[j]] = data1[j]
    data_list.append(dict1)
print(data_list)
f.close()