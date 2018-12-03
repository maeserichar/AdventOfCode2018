#!/usr/bin/python

def process(line):
  d = {}
  for char in line:
    d[char] = d.get(char, 0) + 1

  two = 0
  three = 0

  for (k,v) in d.items():
    if v == 2:
      two = 1
    if v == 3:
      three = 1

  return (two,three)


file = open('input.txt')
twos = 0
threes = 0

for line in file:
  two, three = process(line)
  twos += two
  threes += three

checksum = twos * threes

print('The checksum is ' + str(checksum))
