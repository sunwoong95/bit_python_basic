# import -> 가장 최상단에 위치해야함.
import random
from datetime import datetime
# 0*45 <= random*45 < 1*45
def make_int (x:float):
    x = str(x).split(".")
    return int(x[0])
#랜덤 리턴 값 정수로 만들기.
#로또 번호 뽑기.
lotto = []
while len(lotto) != 6:
    ran_num  = make_int(random.random()*45+1)
    num_pass = True
    for j in lotto:
        if j  == ran_num:
            print(f"겹치는 번호 : {j}")
            num_pass = False
            break
    if num_pass:
        lotto.append(ran_num)
print(lotto)

# import datetime
# print(datetime.datetime(2022,11,4).today())
print(datetime.today())