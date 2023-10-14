def GetCodes(file):
  # Get input from text file
  with open(file, 'r') as f:
    codes = f.readlines()

  
  return(codes)

def split(word): 
    return [char for char in word]


andy_inp = GetCodes('AndyInput')
sim_inp = GetCodes('SimInput')
inp = sim_inp
x = 0
currentLine = ''

def slopeCheck(xSlope, ySlope):
  trees = 0
  i = 0
  o = 0
  while(i < len(inp)):
    x = o*xSlope
    
    currentLine = inp[i]
    
    split(currentLine)
    
    while(x >= 31):
      x -= 31
    
    if(currentLine[x] == '#'):
      trees += 1
      
    i += ySlope
    o += 1
  return(trees)

slopeOne = slopeCheck(1,1)
print(slopeOne)
slopeTwo = slopeCheck(3,1)
print(slopeTwo)
slopeThree = slopeCheck(5,1)
print(slopeThree)
slopeFour = slopeCheck(7,1)
print(slopeFour)
slopeFive = slopeCheck(1,2)
print(slopeFive)
print(slopeOne*slopeTwo*slopeThree*slopeFour*slopeFive)






