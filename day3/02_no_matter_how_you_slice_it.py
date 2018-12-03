#! /usr/bin/python
import re

SIZE = 1000
REGEX = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

fabric = [[set() for x in range(SIZE)] for y in range(SIZE)]

file = open('input.txt')

last_procesed = 0
for line in file:
  match = REGEX.match(line)
  id = int(match.group(1))
  x = int(match.group(2))
  y = int(match.group(3))
  i = int(match.group(4))
  j = int(match.group(5))
  for a in range(x, x+i):
    for b in range(y, y+j):
      fabric[a][b].add(id)
  last_procesed = id

candidates = set(range(1, last_procesed + 1))

for x in range(0, SIZE):
  for y in range(0, SIZE):
    if len(fabric[x][y]) > 1:
      candidates = candidates.difference(fabric[x][y])

print(str(candidates))
