with open('day2/example_data.txt','r',newline='') as f:
    data = f.read().splitlines()
    current_position = [0,0]
    for d in data:
        direction = d.split(' ')[0]
        distance = int(d.split(' ')[1])
        if direction == "forward":
          current_position[0] = current_position[0]+distance
        if direction == "down":
          current_position[1] = current_position[1]+distance
        if direction == "up":
          current_position[1] = current_position[1]-distance
print(current_position)
print(current_position[0]*current_position[1])