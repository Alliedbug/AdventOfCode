correctPasswords = 0
i = 0
test_var = '14-15 v: vdvvvvvsvvvvvfpv'


def GetCodes(file):
  # Get input from text file
  with open(file, 'r') as f:
    codes = f.readlines()
  
  return(codes)

andy_inp = GetCodes('AndyInput')
sim_inp = GetCodes('SimInput')
inp = sim_inp

def split(word): 
    return [char for char in word]
def sort_input(input):
  inp_list = []
  input = input.split('-')
  minimum = input[0]
  input = input[1].split(' ')
  maximum = input[0]
  password = input[2]
  input = input[1].split(':')
  letter = input[0]
  inp_list.extend((minimum,maximum,letter,password))
  return(inp_list)


ans = 0
while(i < len(inp)):
  currentPassword = sort_input(inp[i])
  pos1 = int(currentPassword[0])
  pos2 = int(currentPassword[1])
  letter = currentPassword[2]
  password = currentPassword[3].strip('\n')
  sorted_pass = split(password)
  
  if (sorted_pass[pos1-1] == letter) ^ (sorted_pass[pos2-1] == letter):
    ans += 1
  i += 1

print(ans)