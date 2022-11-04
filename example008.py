# while 반복문
ran = []

i = 0
while False :
    ran.append(i)
    i = i + 1
for j in ran:#range(0,5) = ran
    print()

#print(ran)
#print(list(range(0,5))) # [0,1,2,3,4]

k = 0
while False:
    q = 0
    while q < 10:
        if (k % 2 > 0):
            q += 1
            break
        elif(k % 10 == 0):
            break
        print("q",q)
        q += 1
    print("k",k)
    k += 1

p = [4,3,2,1]
tmp = p[1] #3
p[1] = p[2] #[4,2,2,1]
p[2] = tmp #[4,2,tmp=3,1]
# print(p)

p[1],p[2] = p[2],p[1]
# print(p)

p = [1,2,3,4,5,6]
for i in range(0, len(p)):
    num_max = p[i]
    for j in range(i+1, len(p)):
        if num_max < p[j]:
            num_max = p[j]
            p[i],p[j] = p[j],p[i]            
#print(p)

p = [1,2,3,4,5,6]
p_len = len(p)
o = []
for i in range(0, p_len):
    p_max = max(p)
    o.append(p_max)
    p.remove(p_max)
#print(o)

p = [1,2,3,4,5,6]
p.reverse()
#print(p)

def sum(a:int,b:int):
    try:
        return a+b
    except:
        return "이상한거"

#print(sum(1,2))
#print(sum("hi",2))

def diff(a, b):
    print(a)
    if a - b == 1:
        return [a,b]
    else:
        return diff(a-b,b) #재귀 

# print(diff(100,1))

p = [1,2,3,4,5,6]
p_len = len(p)
o = []
for i in range(0, p_len):
    p_max = max(p)
    o.append(p_max)
    p.remove(p_max)
# print(o)

def nummax (a:list,b:list):
    if(len(a) == 0):
        return b
    a_max = max(a)
    b.append(a_max)
    a.remove(a_max)
    return nummax(a,b)

p = [1,2,3,4,5]
t = []
# print(nummax(p,t))

def sum_func(*nums): #tuple
    i=0
    for num in nums:
        i+=num
    return i
# print(sum_func(1,2,3,4))
# print(sum_func(1,2,3,4,7,8,9,1))
# print(sum_func(1))

def person( a,*nums, **info):
    print(a)
    print(nums)
    return info
# print(person("dd", 1,2,3,name="park"))

a="a b c"

def space_to_list(a:str):
    b = []
    for i in a:
        if i != " ":
            b.append(i)
    return b
        
# print(space_to_list(a))
# a = "a b c"
# b=a.split("")
# print(b)
