import random
from datetime import datetime
f = open("./../csv_file/lotto.txt","w",encoding="utf-8")
def make_int (x:float):
    x = str(x).split(".")
    return int(x[0])
lotto = []
make_num = []
while len(make_num) != 30:
    ran_num  = make_int(random.random()*45+1)
    num_pass = True
    for j in lotto:
        if j  == ran_num:
            print("중복")
            num_pass = False
            break
    if num_pass:
        make_num.append(ran_num)
print(make_num)
for i in range(0,len(make_num)):
    line_pass =True
    if line_pass:
        lotto.append(make_num[i])
    if len(lotto) == 6:
        f.write(str(lotto)+"\n")
        line_pass = False
        lotto = []
        lotto.append(make_num[i])

f.write(f"\n출력시간 : {(datetime.today()).replace(microsecond=0)}")

f.close()