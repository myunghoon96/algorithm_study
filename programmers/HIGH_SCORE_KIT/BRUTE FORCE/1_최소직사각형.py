# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    widths = []
    heights = []

    for size in sizes:
        w, h = max(size), min(size)
        widths.append(w)
        heights.append(h)

    return max(widths) * max(heights)
