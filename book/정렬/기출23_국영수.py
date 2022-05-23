# https://www.acmicpc.net/problem/10825
import sys
input = sys.stdin.readline

n = int(input())

infos = []
for _ in range(n):
    name, kr, en, math = input().split()
    infos.append([name, -1*int(kr), int(en), -1*int(math) ])

infos.sort(key = lambda x: (x[1], x[2], x[3], x[0]))

for e in infos:
    print(e[0])
