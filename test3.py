def make_data(file_name:str,mode:str):
    f = open(file_name,mode,encoding="utf-8")
    total_data = f.readlines()
    data_keys = total_data[0].strip().split(",")
    data_list = []

    for i in range(1,len(total_data)):
        data1 = total_data[i].strip().split(",")
        dict1 = {}
        for j in range(0, len(data1)):
            dict1[data_keys[j]] = data1[j]
        data_list.append(dict1)
    f.close()
    return data_list

def high_avg(data_list:list,key:str,list_avg:int):
    avg_person_list=[]
    for i in data_list:
        if int(i.get(key)) > list_avg:
            avg_person_list.append(i)
    return avg_person_list

def avg_data(data_list:list,key:str):
    total_make = 0
    for i in range(0,len(data_list)):
        total_make += int(data_list[i].get(key))
    make_avg = total_make/len(data_list)
    return int(make_avg)

key = "price"

data_list = make_data("./../csv_file/9898.csv","r")

avg_list = avg_data(data_list,key)

print(data_list)
print(avg_list)
print(key)
print(high_avg(data_list,key,avg_list))