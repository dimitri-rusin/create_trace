# Just a developer tool: to generate a trace of the Python script,
# that is more detailed than print commands deliver.
import inspect
def info(value):

  # Get the expression, via which 'value' is brought here.
  # How is the value expressed in the Python language?
  frame = inspect.currentframe()
  expressions = inspect.getframeinfo(frame.f_back).code_context
  line_number = inspect.getframeinfo(frame.f_back).lineno
  expression = expressions[0]
  left_index = expression.find('(') + 1 # jump over the opening parenthesis
  right_index = -2 # the ')\n' symbols are at the last 2 positions of the string
  expression = expression[left_index:right_index]

  print('---------------------------------------------------------------')

  # Show the given expression of the value
  print(f'{expression} at line {line_number}')

  # Show the type of the value.
  try: print(f'  type: {type(value)}')
  except: pass

  # Show the number of elements of the value, if possible.
  try: print(f'  len: {len(value)}')
  except: pass

  # Show the type of the first element inside of the iterable value, if possible.
  try: print(f'  type[0]: {type(value[0])}')
  except: pass

  # Show the class methods of the value.
  try: print(f'  dir: {dir(value)}')
  except: pass

  # Show the class attributes of the value.
  try: print(f'  dict: {value.__dict__}')
  except: pass

  # Show the value itself.
  try: print(f'  value: {value}')
  except: pass

import pdb
def breakpoint():
  pdb.set_trace()
