#!/usr/bin/python

import re

date = '\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\]'
begin_shift = re.compile(date + ' Guard #(\d+) begins shift')
falls_sleep = re.compile(date + ' falls asleep')
wakes_up = re.compile(date + ' wakes up')

times = {}
start = -1
current = -1
file = open('input.txt')

lines = sorted(file.readlines())

for line in lines:
  begins_match = begin_shift.match(line)
  if begins_match != None:
    current = int(begins_match.group(2))
  falls_match = falls_sleep.match(line)
  if falls_match != None:
    start = falls_match = int(falls_match.group(1))
  wakes_match = wakes_up.match(line)
  if wakes_match != None:
    end = int(wakes_match.group(1))
    if current not in times:
      times[current] = [0 for _ in range(0,60)] 
    for x in range(start, end):
      times[current][x] += 1

max_hours = -1
max_minute = -1
max_guard = -1
for guard in times:
  for i in range(0, len(times[guard])):
    if times[guard][i] > max_hours:
      max_hours = times[guard][i]
      max_guard = guard
      max_minute = i

print(max_guard)
print(max_minute)
print(str(max_guard * max_minute))
