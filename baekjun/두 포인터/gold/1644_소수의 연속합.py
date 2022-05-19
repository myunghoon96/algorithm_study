# https://www.acmicpc.net/problem/1644

n = int(input())
ans = 0

#에라토스테네스의 체
def generate_prime_list(num):
    num = num + 1
    check_list = [True] * num

    for i in range(2, int(num**0.5)+1):
        if check_list[i]:
            for j in range(i+i, num, i):
                check_list[j] = False
    
    prime_list = []
    for idx in range(2,num):
        if check_list[idx]:
            prime_list.append(idx)

    return prime_list

prime_nums = generate_prime_list(n)
       
if len(prime_nums) == 0:
    print(0)
    exit(0)

l, r = 0, 0
tmp_sum = prime_nums[0]
while True:
    if tmp_sum == n:
        # print(prime_nums[l], prime_nums[r])
        ans += 1
        tmp_sum -= prime_nums[l]
        l += 1
        if l == len(prime_nums):
            break
    elif tmp_sum < n:
        r += 1
        if r == len(prime_nums):
            break
        tmp_sum += prime_nums[r]
    elif tmp_sum > n:
        tmp_sum -= prime_nums[l]
        l += 1
        if r == len(prime_nums):
            break


print(ans)