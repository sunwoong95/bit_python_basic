import random
from datetime import datetime
f = open("./../csv_file/lotto.txt","w",encoding="utf-8")
def make_int (x:float):
    x = str(x).split(".")
    return int(x[0])
# 0*45 <= random*45 < 1*45
#랜덤 리턴 값 정수로 만들기.
#로또 번호 뽑기.
for i in range(0,5):
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
    for i in range(0,6):
        if i < 5:
            f.write(str((lotto)[i])+",")
        elif i == 5:
            f.write(str((lotto)[i])+"\n")

# import datetime
# print(datetime.datetime(2022,11,4).today())
f.write("\n출력시간 : " + str(datetime.today().replace(microsecond=0)))
f.close()