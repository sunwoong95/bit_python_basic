my_money = 43250
a=[10000,5000,1000,500,100,50,10]

for money in a:
    if(my_money//money >= 1):
        print(f"{money}원짜리는 {my_money//10000}장이고")
        my_money -= (my_money//money)*money
    elif(my_money//money == 0):
        print(f"{money}원짜리는 0장이고")
