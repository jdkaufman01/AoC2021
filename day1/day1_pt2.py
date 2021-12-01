with open('day1/puzzle_data.txt','r',newline='') as f:
    data = [int(x) for x in f.read().splitlines()]
result = 0
group_sums = []

for i in range(len(data)):
    group = data[i:(i+3)]
    group_sum = sum(group)
    group_sums.append(group_sum)

for i in range(len(group_sums)):
    if i != 0:
      if 0 < (int(group_sums[i]) - int(group_sums[i-1])):
          print("Increased")
          result = (result + 1)
      else:
          print("Decreased")

print(result)