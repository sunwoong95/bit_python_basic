#(클래스class) (oop객체지향)
# a =[]
# a.pop

# clss 여러개의 기능을 가지고 있는거.
# python 에서는 @ = 데코레이션
# @overload
# overload = 하나의 이름으로 변수에 따라 기능이 달라진다.

# def sum(a:int):
#     return a
# def sum(a:str):
#     return a

# print(sum("hi"))
# print(sum(1))

# default = 기본값.

# print({"name":"kim"}.get("age","없어"))
# print({"name":"kim"}.get("name","없어"))

# @final = 수정 불가 class

# range(start, stop, [step])

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def range(start,end):
#     i=start
#     a=[]
#     while i != end:
#         a.append(i)
#         i+=1
#     return a

# [0, 2, 4, 6, 8]
# @overload
# def range(start,end,step=1): #sterp=1 -> default 값으로 진행.
#     i=start
#     a=[]
#     while i <= end:
#         a.append(i)
#         i+=step
#     return a

# print(range(0,10))
# for i in range(0,5,2):
#     print(i)

# open input

# while True:
#     num = input()
#     if num in 

# num = input("숫자를 입력해줘:")
# num1 = input("숫자를 입력해줘:")

# print("print",int(num)+int(num1))

# open = 파일 오픈.
# 1.open =====> 2.(쓰기, 읽기, 저장)

# def sum(a=0,b=0,c=0,type="sum"):
#     if type == "sum":
#         return a+b+c
#     else:
#         return a-b-c

# print(sum(a=1,b=2,type="ss"))

# f = open("test.txt","w")
# a = []
# for i in range(0,10):
#     f.write(f"{str(i)}\n")
#     # f.write(str(i+1)+"\n")
#     a.append(input("입력 : "))
# for el in a:
#     f.write(el+"\n")

# # for i in range(0,10):
# #     f.write(f"{str(i)}\n")
# #     # f.write(str(i+1)+"\n")
# f.close()

# f = open("test.txt","w")

# f.close()
# # f.write("aaaaaaaaa") # file close error

# f = open("test.txt","w")
# while True:
#     x = input("입력 : ")
#     if x == "end":
#         break
#     f.write(str(x)+"\n")
# f.close()

# f = open("test.txt","r")
# while True:
#     # str == "" (False)
#     # input("ddd") => "ddd\n"
#     x = f.readline()
#     if x:
#         print(x.strip())
#     else:
#         break
# f.close()

# print(("ddd\n").strip())
# print(("ddd\n").strip())

# f = open("test.txt","r")
# # print(f.readlines())
# for line in f.readlines():
#     print(str(line).strip())
# f.close()

#file update
#csv 에서 데이터 만드는 법.

# f = open("test.txt","w",encoding="utf-8")
# f.write("글을 쓴다\n")
# f.close()

# f = open("test.txt","a",encoding="utf-8") #a = append
# f.write("글을 쓴다2\n")
# f.close()

# w = write , r = read , a = append.
# 글자 오류 = encoding.
# 파일은 언제나 마지막에 close로 닫기.

# f = open("9898.csv","w",encoding="utf-8")
# person = {"name":"kim","age":15},
# f.write(("name,age")+"\n")
# f.write(("kim,15")+"\n")
# f.write(("park,18")+"\n")
# f.write(("lee,19")+"\n")
# f.write(("kim,15")+"\n")
# f.write(("park,18")+"\n")
# f.write(("lee,19")+"\n")
# f.close()

# . = 현위치
# .. = 상위 위치
# cd = click directory
# ./csv/9898.csv
# C:\python_q\csv_file\9898.csv 절대 경로
# csv_file\9898.csv 상대 경로

f = open("./csv/9898.csv","r",encoding="utf-8")
total_data = f.readlines()
data_keys = total_data[0].strip().split(",")
data_list = []
# data1 = total_data[1].strip().split(",")
# data2 = total_data[2].strip().split(",")
# dict1 = {data_keys[0]:data1[0],data_keys[1]:data1[1]}
# dict2 = {data_keys[0]:data2[0],data_keys[1]:data2[1]}
for i in range(1,len(total_data)):
    data1 = total_data[i].strip().split(",")
    dict1 = {}
    print ("data1",data1)
    for j in range(0, len(data1)):
        dict1[data_keys[j]] = data1[j]
    data_list.append(dict1)
    print(dict1)
# print(data1)

f.close()

