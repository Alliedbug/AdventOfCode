numFile = open("numandy", 'r') #Open the file
nums = ''

nums = numFile.read() #Read file and put into nums
backup = nums




output = 19690720
memory = 0
answer = 0
noun = 0
verb = 0
f = 0


print(nums)
while answer != output:
  nums = backup
  nums = nums.split(',')

  f = -1 
  for i in nums: #Cast type str into int
    f = f+1
    nums[f] = int(nums[f])
  if noun == 100:
    noun = 0
    verb = verb + 1
  nums[1] = noun
  nums[2] = verb
  x = len(nums)
  f = -1
  y = 0
  print(nums)
  while y < x:
    f = f+1
    if nums[f] == 1: #looks at first number in sequence of 4
      f = f+1
      pos1 = nums[f] #looks at second number in sequence of 4 and stores it in pos1
      f = f+1
      pos2 = nums[f] #looks at third number in sequence of 4 and stores it in pos2
      add1 = nums[pos1] #takes the number at position of the second number and stores it in a variable
      add2 = nums[pos2] #takes the number at position of the third number and stores it in a variable
      answer = add1 + add2 #adds to numbers to get answer
      f = f+1
      endPos = nums[f] #looks at 4th number and stores it in endPos
      nums[endPos] = answer #puts the answer at the final position
    elif nums[f] == 2:
      f = f+1
      pos1 = nums[f]
      f = f+1
      pos2 = nums[f]
      mult1 = nums[pos1]
      mult2 = nums[pos2]
      answer = mult1*mult2
      f = f+1
      endPos = nums[f]
      nums[endPos] = answer
    elif nums[f] == 99:
      print(nums)
      answer = nums[0]
      print(answer)
      y = 10000
  if nums[0] == 19690720:
    print(noun)
    print(verb)
  else:
    noun = noun+1