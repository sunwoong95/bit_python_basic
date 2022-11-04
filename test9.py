import random
from datetime import datetime
file = open("./../csv_file/lotto.txt","w",encoding="utf-8")

def make_int (x:float):
    x = str(x).split(".")
    return int(x[0])

def makes_six_number():
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
    return lotto

for i in range(0,5):
    lotto = makes_six_number()
    for j in range(0,len(lotto)):
        if j == len(lotto)-1:
            file.write(f"{lotto[j]}\n")
        elif j < len(lotto):
            file.write(f"{lotto[j]},")

file.write("\n출력시간 : " + str(datetime.today().replace(microsecond=0)))
file.close()