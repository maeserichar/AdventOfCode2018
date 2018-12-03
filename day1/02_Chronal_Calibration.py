#!/usr/bin/python
# -*- encoding: utf-8 -*-

frequency = 0

already_seen = set()

while True:
  input = open('input.txt')
  for line in input:
    drift = int(line)
    frequency = frequency + drift
    
    if (frequency in already_seen):
      print('The repeated frequency is ' + str(frequency))
      exit()
    else:
      # print('Frequency ' + str(frequency) + ' not seen')
      already_seen.add(frequency)

print('The final frequenty is ' + str(frequency) + ' but no repetition found¿?¿')  

