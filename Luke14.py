from urllib import request    

# Get note with path    
url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-bounding-crisscross.txt'
note = request.urlopen(url).read().decode('utf-8').strip()

# Initialize 
x, y = 0, 0
x_max, x_min, y_max, y_min = 0, 0, 0, 0
direction = {'F':(0, 1), 'B':(0, -1), 'V':(-1, 0), 'H':(1, 0)}
visited = set((0, 0))
#note = '2H2F2H1B3V'

# Walk path
for i in range(0, len(note), 2):

  # Walk
  distance = int(note[i])
  dx, dy = direction[note[i + 1]]

  for step in range(distance):
    x, y = x + dx, y + dy
    visited.add((x, y))

  # Update max visited coordinates
  x_max = max(x, x_max)
  x_min = min(x, x_min)
  y_max = max(y, y_max)
  y_min = min(y, y_min)

# Calculate ratio
area = (x_max - x_min + 1) * (y_max - y_min + 1)
number_of_visited = len(visited)
#print(number_of_visited)
#print(area - number_of_visited)

#print(y_max, y_min, (y_max - y_min))
#print(x_max, x_min, (x_max - x_min))
ratio = number_of_visited / (area - number_of_visited)

print(round(ratio, 16))
