# -*- coding: utf-8 -*-
"""Puzzle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z5pGVZZh9nBk44Ywx9_fcB-8Do7tOLiC
"""

with open("input.txt", 'r') as read_file:
    numbers = [int(i) for i in read_file.read().splitlines()]

def part1(numbers):
    return sum(j > i for i, j in zip(numbers, numbers[1:]))

def part2(numbers):
    return sum(numbers[i] > numbers[i-3] for i in range(3, len(numbers)))

print("Part1:", part1(nums), "\nPart2:", part2(nums))

