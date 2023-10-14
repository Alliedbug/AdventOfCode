# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# Make sure to add 1 to your end for range function
start = 146810
end = 612565
total = 0
def split(number):
  return list(number)

def isGreater(num):
  if num[0] <= num[1] and num[1] <= num[2] and num[2] <= num[3] and num[3] <= num[4] and num[4] <= num[5]:
    return True

# Iterate through our given range
for num in range(start, end):

  num = str(num)
  num = split(num)
  

  if num[0] == num[1] and num[1] != num[2]:
    if isGreater(num):
      total += 1

  elif num[1] == num[2] and num[2] != num[3] and num[1] != num[0]: 
    if isGreater(num):
      total += 1

  elif num[2] == num[3] and num[3] != num[4] and num[2] != num[1]:
      if isGreater(num):
        total += 1

  elif num[3] == num[4] and num[4] != num[5] and num[3] != num[2]:
      if isGreater(num):
        total += 1

  elif num[4] == num[5] and num[4] != num[3]:
      if isGreater(num):
        total += 1


print(total)




  
