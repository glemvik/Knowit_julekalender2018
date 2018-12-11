from  urllib import request

# Read notes
print('Read')
url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-crisscross.txt'
f = request.urlopen(url)
notes = f.read().decode('utf-8').strip()

directions = {'H':(1, 0), 'V':(-1, 0), 'F':(0, 1), 'B':(0, -1)}

print('Walk')
x, y = 0, 0
index = 0
limit = len(notes)
percentage = 0.01
while index < limit:

    if index / limit > percentage:
        print(percentage * 100, '%')
        percentage += 0.01
    distance = ''
    while index < len(notes[:-1]) and notes[index] not in directions.keys():
        distance += str(notes[index])
        index += 1

    dx, dy = directions[notes[index]]
    index += 1

    x += int(distance) * dx
    y += int(distance) * dy


print(f'[{x},{y}]')
