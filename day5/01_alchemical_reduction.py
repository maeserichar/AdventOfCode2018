#!/usr/bin/python

def react(char1, char2):
  print('We are comparing ' + char1 + ' and ' +char2)
  if (char1.isupper() and char2.islower()) or (char1.islower() and char2.isupper()):
    if char1.lower() == char2.lower():
      print('React!')
      return True
  return False


file = open('test.txt')

solution = []
last_inserted = -1

for line in file:
  for char in line:
    print(last_inserted)
    print(solution)
    print(char)
    if (last_inserted > -1 and react(char,line[last_inserted])):
      solution.pop(last_inserted)
      last_inserted -= 1
    else:
      solution.append(char)
      last_inserted += 1

print(solution)
print('The number of units is ' + str(len(solution)))
