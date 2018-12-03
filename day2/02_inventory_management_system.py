#!/usr/bin/python
import itertools
from itertools import groupby

def hamdist(str1, str2):
  """Count the # of differences between equal length strings str1 and str2"""
  diffs = 0
  for ch1, ch2 in zip(str1, str2):
    if ch1 != ch2:
      diffs += 1
  return diffs

file = open('input.txt')
lines = file.readlines()

for i in range(0, len(lines)):
  for j in range(i + 1, len(lines)):
    dist = hamdist(lines[i], lines[j])
    if dist == 1:
      print lines[i]
      print lines[j]
