# 내가 43250원이 있다.
# 만원짜리는 몇장이고
# 오천원짜리는 몇장이고
# 천원짜리는 몇장이고
# 500원짜리는 몇개이고
# 100원짜리는 몇개이고
# 50원짜리는 몇개이고
# 10원짜리는 몇개있다.

my_money = 43250

if(my_money//10000 >= 1):
    print(f"만원짜리는 {my_money//10000}장이고")
    my_money -= (my_money//10000)*10000
elif(my_money//10000 == 0):
    print(f"만원짜리는 0장이고")

if(my_money//5000 >= 1):
    print(f"오천원짜리는 {my_money//5000}장이고")
    my_money-= (my_money//5000)*5000
elif(my_money//5000 == 0):
    print(f"오천원짜리는 0장이고")        

if((my_money//1000) >= 1):
    print(f"천원짜리는 {(my_money//1000)}장이고")
    my_money -= (my_money//1000)*1000
elif((my_money//1000) == 0):
    print(f"천원짜리는 0장이고")  

if((my_money//500) >= 1):
    print(f"500원짜리는 {(my_money//500)}개이고")
    my_money -= (my_money//500)*500
elif((my_money//500) == 0):
    print(f"500원짜리는 0개이고")

if((my_money//100) >= 1):
    print(f"100원짜리는 {(my_money//100)}개이고")
    my_money -= (my_money//100)*100
elif((my_money//100) == 0):
    print(f"100원짜리는 0개이고")

if(my_money//50) >= 1:
    print(f"50원짜리는 {(my_money//50)}개이고")
    my_money -= (my_money//50)*50
elif(my_money//50) == 0:
    print(f"50원짜리는 0개이고")

if(my_money//10) >= 1:
    print(f"10원짜리는 {(my_money//10)}개이고")
    my_money -= (my_money//10)*10
elif(my_money//10) == 0:
    print(f"10원짜리는 0개 입니다.")



my_money = 43250
a=[10000,5000,1000,500,100,50,10]

for money in a:
    if(my_money//money >= 1):
        print(f"{money}원짜리는 {my_money//10000}장이고")
        my_money -= (my_money//money)*money
    elif(my_money//money == 0):
        print(f"{money}원짜리는 0장이고")
