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
current_max = -1
max_hours = -1

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
      times[current] = { 'count': 0, 'times': [0 for _ in range(0,60)] }
    for x in range(start, end):
      times[current]['times'][x] += 1
    times[current]['count'] += end - start
    if max_hours < times[current]['count']:
      max_hours = times[current]['count']
      current_max = current

print('The guard with more asleep hours is ' + str(current_max))

hours = times[current_max]['times']
max_hour = -1
max_days = 0
for i in range(0, len(hours)):
  if hours[i] > max_days:
    max_days = hours[i]
    max_hour = i

print('The best hour is ' + str(max_hour))

print(str(current_max * max_hour))
