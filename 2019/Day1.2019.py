numFile = open("numsim","r") #reads file

nums = [] #initiates variables
answer = 0
total = 0

f = 0
while f < 100: #takes numbers and puts it into a list - \n
    nums.append(numFile.readline())
    f = f+1
list2 = [x.replace('\n', '') for x in nums] #Removes \n


f = 0 #turns list of strt into int
while f < 100:
  list2[f] = int(list2[f])
  f = f+1

nums = list2

f = 0 #does math stuff
while f < 100:
  nums[f] = nums[f] // 3 - 2
  for i in nums: 
    while nums[f] > 0:
      nums[f] = nums[f] // 3 - 2
      if nums[f] > 0:
        total += nums[f]
        print(nums[f])
        print(total + 3255932)
  f = f+1

f = 0 #adds math things together
while f < 100:
  answer = answer + nums[f]
  f = f+1


  #hello peepee man