# https://www.acmicpc.net/problem/11051
import math

N, K = map(int, input().split())

ans = (math.factorial(N) // (math.factorial(K) * math.factorial(N-K))) % 10007

print(int(ans))