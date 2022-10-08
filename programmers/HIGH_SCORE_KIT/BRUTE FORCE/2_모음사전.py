# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product


def solution(word):
    answer = 0

    letters = ["A", "E", "I", "O", "U"]
    words = []

    for word_length in range(1, 6):
        products = list(product(letters, repeat=word_length))
        words += [''.join(product) for product in products]

    words.sort()
    answer = words.index(word) + 1
    return answer
