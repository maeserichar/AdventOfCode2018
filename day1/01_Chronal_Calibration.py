frequency = 0

input = open('input.txt')

for line in input:
  drift = int(line)
  frequency = frequency + drift

print('The final frequenty is ' + str(frequency))  

