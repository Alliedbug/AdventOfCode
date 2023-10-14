# Open our files
numFile1 = open("numsim", 'r')
numFile2 = open("numsim2", 'r')


# Store our directions in a list
directionList1 = numFile1.read().split(',')  
directionList2 = numFile2.read().split(',') 

# Close our files after we are done reading
numFile1.close()
numFile2.close()

# Use to calculate our length
beforeCalc = []

# Initialize our wire path into a list
wirePath1 = []
wirePath2 = []

# Initialize our coordinate holders
coordinate1 = [0,0]
coordinate2 = [0,0]

# Keeps track of each wire's length (Day Two)
wireLength1 = []
wireLength2 = []

# Initialize our length holder
wireLengthHolder1 = 0
wireLengthHolder2 = 0

# Final answer to Day Two
finalLength1 = []
finalLength2 = []
finalLength = []
# Holds the points where our wires intersect
sameCoordinate = []

# (Path To String) Convert our direction into a string, so we can append it to our wirePath
def pToString(path):
  
  newInt = str(path)
  return newInt

# Find the smallest number in a list (Yes I know I can literally just do .min() okay?!?!?!)
def findSmallest(listInp):
  answer = min(listInp)
  return answer
# (Day One) Retrieves distance of our coordinates from 0,0
def calc(a,b):

  ans = abs(a) + abs(b)
  return(ans)

# Prepares our string to be converted into an integer
def prepareString(stringInp):
  stringInp = stringInp.strip('[')
  stringInp = stringInp.strip(']')
  stringInp = stringInp.replace(' ', '')
  stringInp = stringInp.split(',')
  return stringInp

# Iterate through direction1 and send each point to our path
for direction1 in directionList1:

  # If leading letter is R, this code will add to the X axis of coordinate1
  if 'R' in str(direction1):
    direction = int(direction1.strip('R'))
    while direction != 0:
      direction -= 1
      # Increment by one, and add each new coordinate to the wire path
      coordinate1[0] += 1
      wirePath1.append(pToString(coordinate1))
      # Increment by one, and add each new movement to the wire length
      wireLengthHolder1 += 1
      wireLength1.append(wireLengthHolder1)

  if 'L' in str(direction1):
    direction = int(direction1.strip('L'))
    while direction != 0:
      direction -= 1
      coordinate1[0] -= 1
      wirePath1.append(pToString(coordinate1))
      wireLengthHolder1 += 1
      wireLength1.append(wireLengthHolder1)

  if 'D' in str(direction1):
    direction = int(direction1.strip('D'))
    while direction != 0:
      direction -= 1
      coordinate1[1] -= 1
      wirePath1.append(pToString(coordinate1))
      wireLengthHolder1 += 1
      wireLength1.append(wireLengthHolder1)

  if 'U' in str(direction1):
    direction = int(direction1.strip('U'))
    while direction != 0:
      direction -= 1
      coordinate1[1] += 1
      wirePath1.append(pToString(coordinate1))
      wireLengthHolder1 += 1
      wireLength1.append(wireLengthHolder1)

# Set our length holder back to 0 for our new wire

# Iterate through direction2 and send each point to our path
for direction2 in directionList2:

  if 'R' in str(direction2):
    direction = int(direction2.strip('R'))
    while direction != 0:
      direction -= 1
      coordinate2[0] += 1
      wirePath2.append(pToString(coordinate2))
      wireLengthHolder2 += 1
      wireLength2.append(wireLengthHolder2)

  if 'L' in str(direction2):
    direction = int(direction2.strip('L'))
    while direction != 0:
      direction -= 1
      coordinate2[0] -= 1
      wirePath2.append(pToString(coordinate2))
      wireLengthHolder2 += 1
      wireLength2.append(wireLengthHolder2)

  if 'D' in str(direction2):
    direction = int(direction2.strip('D'))
    while direction != 0:
      direction -= 1
      coordinate2[1] -= 1
      wirePath2.append(pToString(coordinate2))
      wireLengthHolder2 += 1
      wireLength2.append(wireLengthHolder2)

  if 'U' in str(direction2):
    direction = int(direction2.strip('U'))
    while direction != 0:
      direction -= 1
      coordinate2[1] += 1
      wirePath2.append(pToString(coordinate2))
      wireLengthHolder2 += 1
      wireLength2.append(wireLengthHolder2)

# Send our intersecting points to sameCoordinate
for coordinate in wirePath1:
  if coordinate in wirePath2:
    prepareString(coordinate)
    beforeCalc.append(coordinate)
    cordX = int(prepareString(coordinate)[0])
    cordY = int(prepareString(coordinate)[1])
    sameCoordinate.append(calc(cordX,cordY))

print(f"Day One: {findSmallest(sameCoordinate)}")


for count,value in enumerate(beforeCalc, 0):
  wire1Index = wirePath1.index(beforeCalc[count])
  wire2Index = wirePath2.index(beforeCalc[count])
  finalLength1.append(wireLength1[wire1Index])
  finalLength2.append(wireLength2[wire2Index])
  finalLength.append(finalLength1[count] + finalLength2[count])

finalAnswer = min(finalLength)

print(f"Day Two: {finalAnswer}")
