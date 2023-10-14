#STEPS:

#Before running the program, replace position 1 with the value 12 and replace position 2 with the value 2

#1. Scrap file into a list

#2. Read the first number

#3. If 1:
  #a. Read next two integers to find position of which number to add
  #b. Add those numbers, and store the sum in the position that the integer holds

#4. If 2:
  #a Read next two integers to find position of which number to multiply
  #b. Multiply those numbers, and store the product in the position that the next integer holds

#5. If 99:
  #a. Break

#7. Read the next index and place the answer above into this index's value

#8. Step forward by [4] positions

numFile = open("numandy", 'r') #Open the file

nums = ''

nums = numFile.read() #Read file and put into nums
nums = nums.split(',')

f = -1 
for i in nums: #Cast type str into int
  f = f+1
  nums[f] = int(nums[f])




for count, value in enumerate(nums):

  if count % 4 == 0 and value == 1:
    addPos1 = nums[count+1]
    addPos2 = nums[count+2]
    addPos3 = nums[count+3]
    added = nums[addPos1] + nums[addPos2]
    nums[addPos3] = added 

  if count % 4 == 0 and value == 2:
    multPos1 = nums[count+1]
    multPos2 = nums[count+2]
    multPos3 = nums[count+3]
    multed = nums[multPos1] * nums[multPos2]
    nums[multPos3] = multed

  if count % 4 == 0 and value == 99:
    print(nums)
    break





















# x = len(nums)
# f = 0
# while f < x:
#   if nums[f] == 1: #looks at first number in sequence of 4
#     f = f+1
#     pos1 = nums[f] #looks at second number in sequence of 4 and stores it in pos1
#     f = f+1
#     pos2 = nums[f] #looks at third number in sequence of 4 and stores it in pos2
#     add1 = nums[pos1] #takes the number at position of the second number and stores it in a variable
#     add2 = nums[pos2] #takes the number at position of the third number and stores it in a variable
#     answer = add1 + add2 #adds to numbers to get answer
#     f = f+1
#     endPos = nums[f] #looks at 4th number and stores it in endPos
#     nums[endPos] = answer #puts the answer at the final position
#   if nums[f] == 2:
#     f = f+1
#     pos1 = nums[f]
#     f = f+1
#     pos2 = nums[f]
#     mult1 = nums[pos1]
#     mult2 = nums[pos2]
#     answer = mult1*mult2
#     f = f+1
#     endPos = nums[f]
#     nums[endPos] = answer
#   if nums[f] == 99:
#     print(nums)
#     break
#   f = f+1

numFile.close()

#When testing different files, there are different (amounts of) numbers