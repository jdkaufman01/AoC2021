with open('day2/puzzle_data.txt','r',newline='') as f:
    data = f.read().splitlines()
    current_position = [0,0]
    aim = 0
    for d in data:
      direction = d.split(' ')[0]
      distance = int(d.split(' ')[1])
      if direction == "down":
        aim = aim+distance
      if direction == "up":
        aim = aim-distance                 
      if direction == "forward":
        current_position[0] = current_position[0]+distance
        current_position[1] = current_position[1]+(distance*aim)
print(current_position)
print(current_position[0]*current_position[1])