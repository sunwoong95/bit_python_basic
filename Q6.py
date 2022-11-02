# while 무한루프에 빠지기 쉬운 명령어.
# while ~ 동안 반복문.

# i=0
# while i<5:
#     if (i == 3):
#         i = i + 1
#         continue #무한루프
#     print(i) 
#     i = i + 1
# print("끝이다.")
# 0
# 1
# 2
# 4

# i=0
# while i<5:
#     if (i == 3):
#         break #중단
#     print(i)
#     i = i + 1
# print("끝이다.")
# 0
# 1
# 2

# i = 0
# while True:
#     print(f"while")
# i = 0
# while True:
#     if (i == 60000):
#         break
#     print(f"{i}")
#     i += 1

# a = [0,1,3,5,7,9,10,11,13]

# for x in a:
#     if x % 2 > 0:
#         print(f"{x}")

# a = [0,1,3,5,7,9,10,11,13]
# x=0
# while x < len(a):
#     if a[x] == 0:
#            x = x + 1
#            continue
#     if a[x] % 2 > 0:
#         print(f"{a[x]} 홀수")
#     elif a[x] % 2 == 0:
#            print(f"{a[x]} 짝수")
#     x = x + 1

# match case 뭔가 매치되다. (같다)
# like if

# a = [0,1,3,5,7,9,10,11,13]
# x=0
# while x < len(a):
    
#     flag = "짝수"

#     if a[x] == 0:
#         x = x + 1
#         continue

#     if a[x] % 2 == 1:
#         flag = "홀수"

#     match flag:
#         case "홀수":
#             print(f"{a[x]} {flag}")
#         case "짝수":
#             print(f"{a[x]} {flag}")

#     x = x + 1

# 람다 (lambda) 편의성을 위해 만들어진 기능.

# map => list를 새로운 list로 만든다. line84-~line88 = 압축하게하는 것.

# a = [0,1,3,5,7,9,10,11,13]
# b = [0,2,6,10,14,18,20,22,26]
# c = []
# for i in range(0,len(a)):
#     c.append(a[i] * 2) #list 없는거에 추가할때는 .append(입력할값)
# print(c)
# print(a)

# reduce => 합을 구할 때 사용. 

# a = [0,1,3,5,7,9,10,11,13]
# b = [0,2,6,10,14,18,20,22,26]
# c = 0
# for i in range(0,len(a)):
#     c+=a[i]
# print(c)
# print(a)


# filter 필터링

a = [0,1,3,5,7,9,10,11,13]
b = [1,3,5,7,9,11,13]
c = []
for i in range(0,len(a)):
    if a[i] % 2 > 0:
        c.append(a[i])
print(c)