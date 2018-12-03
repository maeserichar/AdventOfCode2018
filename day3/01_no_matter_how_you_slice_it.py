#! /usr/bin/python
import re

SIZE = 1000
REGEX = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

fabric = [[0 for x in range(SIZE)] for y in range(SIZE)]

file = open('input.txt')

for line in file:
  match = REGEX.match(line)
  x = int(match.group(2))
  y = int(match.group(3))
  i = int(match.group(4))
  j = int(match.group(5))
  for a in range(x, x+i):
    for b in range(y, y+j):
      fabric[a][b] += 1

total = 0

for x in range(0, SIZE):
  for y in range(0, SIZE):
    if fabric[x][y] > 1:
      total += 1

print(str(total))
