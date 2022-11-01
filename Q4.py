#반복문
# a = [10,20,30,10,20,30,10,20,30]

# 디버그-txt 참조
# for i in a = 통으로 진행
# for 변수 in range(): = 하나씩 까서 진행
# range(start,stop[,step])
# range(0,len(a)) 0, 1, 2
# 0 <= i < 3
# range(0,leng(a),2)
# step만큼 올라감. 기본 1. -도 가능.
# for i in range(0,len(a),3):
#     print(i)
# print(a)
# for i in range(0,-len(a),-1):
#     #i=i-1
#     print(i)
# print(a)

# a = [5,8,7,9,10]
# #a.sort()
# for i in range(0,len(a)):
#     x = a[i]
#     if(a[i]%2==0):
#         print(f"{x}는 짝수 입니다.")
# #     elif(a[i]%2>0):
# #         print(f"{x}는 홀수 입니다.")

# a = [5,8,7,9,10]

# i = index의 약자.
# # indexof() 안배움.
# # el = element의 약자.
# # fot el element
# # a a[index]
# for el in a:
# #print(el)
#     if(el%2==0):
#          print(f"{el}는 짝수 입니다.")
#     elif(el%2>0):
#          print(f"{el}는 홀수 입니다.")

# #반복문
# list_a = [10,20,30,10,20,30,10,20,30]
# #for 변수 in 리스트 :
# for i in list_a:
#     print(i)
# # 20 <= x < 30
# #range= 범위설정.
# for i in range(0,len(list_a)):
#     print(i)

#print(list(range(20,-5,-1)))

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

# for i in range(5,0,-1):
#     print("*"*i)

# person = {"name":"kim","age":13}
# person1 = {"name":"park","age":15}
# person2 = {"name":"lee","age":16}
# list_a = [person,person1,person2]
#1
# person_execl = [["name","age"],["kim","13"],["park","15"],["lee","16"]]
# keys = person_execl[0]
# datas = person_execl[1:]

# # # print(data)

# # # for data in datas:
# # #     print(data)
# save = []
# for data in datas:
#     tmp = {} #{"name":"kim"} {"name":"kim","age":13}
#     for i in range(0,len(keys)):
#             tmp[keys[i]] = data[i]
#          #keys[0] = "name", data[0} = "kim"
#         #keys[1] = "age", data[1} = "13"
#     save.append(tmp) #[{"name":"kim","age":13}]
# print(save)
# #     #     tmp[keys] = ""
# #     # for el in data:
# #     #     tmp[key] = el

# person_execl = [["name","age"],["kim","13"],["park","15"],["lee","16"]]
# keys = person_execl[0]
# datas = person_execl[1:]
#2
# save = []
# for data in datas:
#     tmp = {} 
#     for key in keys:
#         tmp[key] = ""
#     for data in datas:
#         tmp[] = data
#     save.append(tmp) 
# print(save)

#3
# person_execl = [["kim","13"],["park","15"],["lee","16"]]

# save = []

# for data in person_execl:
#         tmp = {"name":"","age":0}
        
#         for i in range(0,len(list(tmp.keys()))):
#             tmp[list(tmp.keys())[i]] = data[i]
#         save.append(tmp)
# print(save)
# for key in keys:
#     tmp[key] = ""
# for data in datas:
#     for el in data:
# for data in datas:
#     tmp = {}
#     for i in range(0,len(keys)):
#         tmp[keys[i]] = data[i]
        
#     save.append(tmp)
# print(save)

a = [44,42,23,12,29,27,48,78,21,32]

for x in a:
    answer = f"{x}는 "
    if x%2==0 and x%3==0:
            answer += "2와 3의 공배수 입니다."
    elif x%2>0 or x%3>0:
        answer += "2와 3의 공배수가 아닙니다."
        if x%2==0:
            answer += " 2의 배수 입니다."
        elif x%3==0:
            answer += " 3의 배수 입니다."
    print(f"{answer}")

a = [44,42,23,12,29,27,48,78,21,32]
tmp = {
0:{"str":"2와 3의 공배수가 아닌 것은","count":0},
2:{"str":"2와 3의 공배수가 인 것은","count":0},
3:{"str":"2의 배수 인 것은","count":0},
6:{"str":"3의 배수 인 것은","count":0}}
for x in a:
    if x%2==0 and x%3==0:
        tmp[2]['count'] = tmp.get(2).get('count')+1
        if x%2==0:
            tmp[3]['count'] = tmp.get(3).get('count')+1
        else:
            tmp[6]['count'] = tmp.get(6).get('count')+1
    else:
        tmp[0]['count'] = tmp.get(0).get('count')+1
        if x%2==0:
            tmp[3]['count'] = tmp.get(3).get('count')+1
        else:
            tmp[6]['count'] = tmp.get(6).get('count')+1
for key in list(tmp.keys()):
    tmp2 = tmp.get(key)
    print(f"{tmp2.get('str')}{tmp2.get('count')}개입니다")


# a = [44,42,23,12,29,27,48,78,21,32]
# c = []
# d = []

# for x in a:
#   tmp = {}
#     for y in range(0,len(a)):
#         if x%2==0:
#             c(y)=x
#         else:
#             d(y)=x
# print(f"짝수는 {len(c)+1}개 입니다.")
# print(f"홀수는 {len(d)+1}개 입니다.")

# a = [44,42,23,12,29,27,48,78,21,32]
# b = {0:{"str":"짝수","count":0},1:{"str":"홀수","count":0}}

# for x in a:
#     if x%2==0:
#         b[0]['count']=b.get(0).get("count")+1
#     else:
#         b[1]['count']=b.get(1).get("count")+1

# print(b)
# print("짝수는 {len(c)+1}개 입니다.")
# print("홀수는 {len(d)+1}개 입니다.")