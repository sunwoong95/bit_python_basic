def solution(n:int):
    c = []
    ct = [0,0,0,0,0,0,0,0,0,0]
    for j in range(0,n):
        num = j+1
        for i in str(num):
            k = int(i)
            ct[k] = ct[k] + 1
    answer = f"페이지는 {n}"
    for k in str(n):
        new_k = int(k)
        answer +=  f"\n{k}의 개수는 {ct[new_k]}"
    return answer
print(solution(254))

def solution(n:int):
    b = []
    c = []
    count1 = 0
    count9 = 0
    for i in range(0,n+1):
            i=str(i)
            b.append(i)
    for j in range(0,len(b)):
        num = b[j]
        for i in str(num):
            c.append(i)
    for k in range(0,len(c)):
        if c[k] == "1":
            count1 += 1
        elif c[k] == "9":
            count9 += 1

    return f"페이지는 {n} \n1의 개수는 {count1} \n9의 개수는 {count9}"
print(solution(19))