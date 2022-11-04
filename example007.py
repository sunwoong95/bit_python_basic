# 함수
# def sum(a:int, b:int): # 매개 변수
#     try: # 시도하다.
#         #print(a)
#         #print(b)
#         return a + b
#     except: # 예외
#         return"에러"



# print(sum(1,2)) #1,2 인수  #3
# print(sum("hi",2))
# print(sum(3,4))
# print(sum(5,6)) 
# print(sum(7,8))

# def filtering(a):
#     c = []
#     # a.
#     for i in range(0,len(a)):
#         if a[i] % 2 > 0:
#             c.append(a[i])
#     return c
# list1 = [0,1,3,5,7,9,10,11,13]
# list2 = [1,3,5,7,9,11,13,7,77]
# list3 = [13,9,2,1,3,8,19,20,15]
# list4 = "100"
# print(filtering(list1))
# print(filtering(list2))
# print(filtering(list3))
# # print(filtering(list4))
# # c = []
# # for i in range(0,len(a)):
# #     if a[i] % 2 > 0:
# #         c.append(a[i])
# # print(c)
# def filtering(a:list):
#     c = []
#     a.append()
#     for i in range(0,len(a)):
#         if a[i] % 2 > 0:
#             c.append(a[i])
#     return c

# def diff(a:int,b:int):
#     answer = ""
#     try:
#       dif = a - b
#       if dif < 0:
#         answer = 0
#       else:
#         answer = dif
#     except:
#         answer = "잘못된 거"
#     finally:
#         return answer
   
# # print(diff(1,4))
# # print(diff(7,4))
# # print(diff("hi",4))
# print(diff(diff(1,3),diff(4,5)))

# # def diff(a:int,b:int):
# #     answer = ""
# #     try:
# #         dif = a - b
# #         if dif < 0:
# #             answer = 0
# #         else:
# #             answer = dif
# #     except:
# #         answer = "잘못된 거"
# #     finally:
# #         return answer

# def sum(*nums):# * = tuple trans
#     # print(type(nums))
#     answer = 0
#     for num in nums:
#         answer = answer + num
#     return answer

# print(sum(1,2,3,4,5,6))
# print(sum(5,6,7))
# pe  = [] #전역변수
# def make_profile(**a):
#     # del a["age"]# ** = dic trans
#     # # print(a)
#     # return a# return 값x none 표시.
# def peoples(*t_peoples):
#     answer = list(t_peoples) #지역변수
#     for p in t_peoples:
#         pe.append(p)
#     # a = {"peoples": list(t_peoples), "count":len(t_peoples)}
#     return answer
# # def peoples(*t_peoples):
#     # a = {"peoples": list(t_peoples), "count":len(t_peoples)}
#     # return list(t_peoples)
#         # a = []
#     # for people in t_peoples:
#     #     a.append(people)
#     # return a
# # print(make_profile(name="park",age=20,company="naver"))
# peoples(
#     make_profile(name="park",age=20,company="naver"),
#     make_profile(name="apark",age=10,company="anaver"),
#     make_profile(name="bpark",age=17,company="bnaver"))
 
# # print(pe.get("peoples"))
# # print(pe.get("count"))
# peoples(
#     make_profile(name="park",age=20,company="naver"),
#     make_profile(name="apark",age=10,company="anaver"),
#     make_profile(name="bpark",age=17,company="bnaver"),
#     make_profile(name="cpark",age=22,company="cnaver"))


# pe = {"peoples": [], "count":0}
# pe["peoples"] = peoples(
#     make_profile(name="park",age=20,company="naver"),
#     make_profile(name="apark",age=10,company="anaver"),
#     make_profile(name="bpark",age=17,company="bnaver"),
#     make_profile(name="cpark",age=22,company="cnaver"))

# print(pe)

# 함수 정의
#def 이름(매개변수):
#def print(st)
#print("hi") -> 함수. "hi"->인수.
#def print(*) -> tuple trans
#print("hi","hello",1,2,3)
#def print(n**st) -> dic trans
#print(name = "kim", age = 20)

