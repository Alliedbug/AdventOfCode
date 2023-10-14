i = 0
x = 0
y = 0

def GetCodes(file):
  # Get input from text file
  with open(file, 'r') as f:
    codes = f.readlines()

  # Strip all newlines and typecast from str to int
  codes = [line.strip() for line in codes]
  codes = [int(line) for line in codes]
  return(codes)

andy_inp = GetCodes('AndyInput')
sim_inp = GetCodes('SimInput')

inp = andy_inp
while(i < 200):
  while(x < 200):
    while(y < 200):
      if(inp[i] + inp[x] + inp[y] == 2020):
        print(inp[i])
        print(inp[x])
        print(inp[y])
        print(inp[i]*inp[x]*inp[y])
      y += 1
    x += 1
    y = 0
  i += 1
  x = 0








