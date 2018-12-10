# Code for translation
code = """      :
      |
'.___/i\___.'
  \* \ / */
   ]~~K~~[
  /*_/ \_*\
.'   \*/   '.
      |
      :"""

# Snø++ commands
commands = {' ':lambda x: x + [31], 
            ':':lambda x: [sum(x)], 
            '|':lambda x: x + [3], 
            '\'':lambda x: x[:-2] + [sum(x[-2:])], 
            '.':lambda x: x[:-2] + [x[-1] - x[-2], x[-2] - x[-1]],
            '_':lambda x: x[:-2] + [x[-1] * x[-2], x[-1]],
            '/':lambda x: x[:-1], 
            'i':lambda x: x + [x[-1]], 
            '\\':lambda x: x[:-1] + [x[-1] + 1], 
            '*':lambda x: x[:-2] + [x[-1] // x[-2]], 
            ']':lambda x: x[:-1] + [1 for i in x[-1:] if i % 2 == 0], 
            '[':lambda x: x[:-1] + [1 for i in x[-1:] if i % 2 == 1], 
            '~':lambda x: x[:-3] + [max(x[-3:])]}

# Initialize
index = -1
limit = len(code)
stack = []

# Read code
while index < limit - 1:

  # Get next command
  index += 1
  command = code[index]
  
  # New line
  if command == '\n':
    continue

  # Comment
  elif command == 'K':
    while command != '\n':
      index += 1
      command = code[index]

  # Operations
  else:
    stack = commands[command](stack)

# Result
largest_number = max(stack)
print(largest_number)
