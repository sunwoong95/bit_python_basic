import random
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
            print(f"겹치는 번호 : {j}")
            num_pass = False
            break
    if num_pass:
        make_num.append(ran_num)
f.write(str(lotto))

f.close()




    lotto [[],[],[],[],[]]


    error_lotto = True
if lotto[i][j] == lotto[][]
    error_lotto == False
    break
if error_lotto:
    f.write(str(lotto))