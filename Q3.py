# and or
# and 둘다 만족.
# or 둘중 하나 또는 둘다 만족.
# 12
a = 15

if (a%2==0 and a%3==0):
    print(f"{a}는 2와 3의 공배수 입니다.")
elif (a%2 > 0 or a%3 > 0):
    print(f"{a}는 2와 3의 공배수가 아닙니다.")
    if (a%2 == 0):
        print(f"{a}는 2의 배수입니다.")
    elif (a%3 == 0):
        print(f"{a}는 3의 배수입니다.")

# print(f"{a}는 2와 3의 공배수 입니다.")
# print(f"{a}는 2와 3의 공배수가 아닙니다.")
# print(f"{a}는 2의 배수입니다.")
# ptint(f"{a}는 3의 배수입니다.")