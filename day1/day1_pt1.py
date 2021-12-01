with open('day1/puzzle_data.txt','r',newline='') as f:
    data = f.read().splitlines()
result = 0

for i in range(len(data)):
    if i != 0:
      if 0 < (int(data[i]) - int(data[i-1])):
          print("Increased")
          result = (result + 1)
      else:
          print("Decreased")

print(result)