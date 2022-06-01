# https://www.acmicpc.net/problem/6588

#에라토스테네스의 체
def generate_prime_list(num):
    num = num + 1
    check_list = [True] * num

    for i in range(2, int(num**0.5)+1):
        if check_list[i]:
            for j in range(i+i, num, i):
                check_list[j] = False
    
    # prime_list = []
    # for idx in range(2,num):
    #     if check_list[idx]:
    #         prime_list.append(idx)

    return check_list

prime_nums = generate_prime_list(1000000)
prime_nums[1] = False
prime_nums[2] = False

while True:
    num = int(input())

    if num == 0:
        break

    flag = False
    for i in range(num):
        if prime_nums[i] and prime_nums[num-i]:
            print(num, "=", i, "+", num-i)
            flag = True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")
