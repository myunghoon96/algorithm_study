# https://programmers.co.kr/learn/courses/30/lessons/92335

def convert(n, k):

    result = ''
    while n > 0:
        
        div = n // k
        mod = n % k
        # print(n, div, mod)
        n = div
        result += str(mod)

    return result[::-1]

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    num_str = convert(n, k)
    # print(num_str)
    num_list = num_str.split('0')
    # print(num_list)
    
    for num in num_list:
        if num == "":
            continue
        # print(int(num))
        if check_prime(int(num)):
            # print(num)
            answer += 1
    return answer