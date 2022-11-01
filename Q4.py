#반복문
# a = [10,20,30,10,20,30,10,20,30]

# 디버그-txt 참조

# for 변수 in range():
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

a = [5,8,7,9,10]
for i in range(0,len(a)):
    x = a[i]
    if(a[i]%2==0):
        print(f"{x}는 짝수 입니다.")
    elif(a[i]%2>0):
        print(f"{x}는 홀수 입니다.")