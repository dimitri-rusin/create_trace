# Just a developer tool: to generate a trace of the Python script,
# that is more detailed than print commands deliver.
import inspect
import colored
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
  print(f'''{colored.stylize(expression, colored.fg('green_1'))} at line {colored.stylize(f'{line_number}', colored.fg('green_1'))}''')

  # Show the type of the value.
  opening_name = colored.stylize("type: ", colored.bg("dark_cyan"))
  closing_name = colored.stylize(" :type", colored.bg("dark_cyan"))
  try: print(f'  {opening_name}{type(value)}{closing_name}')
  except: pass

  # Show the number of elements of the value, if possible.
  opening_name = colored.stylize("len: ", colored.bg("dark_cyan"))
  closing_name = colored.stylize(" :len", colored.bg("dark_cyan"))
  try: print(f'  {opening_name}{len(value)}{closing_name}')
  except: pass

  # Show the type of the first element inside of the iterable value, if possible.
  opening_name = colored.stylize("type[0]: ", colored.bg("dark_cyan"))
  closing_name = colored.stylize(" :type[0]", colored.bg("dark_cyan"))
  try: print(f'  {opening_name}{type(value[0])}{closing_name}')
  except: pass

  # Show the class methods of the value.
  opening_name = colored.stylize("dir: ", colored.bg("dark_cyan"))
  closing_name = colored.stylize(" :dir", colored.bg("dark_cyan"))
  try: print(f'  {opening_name}{dir(value)}{closing_name}')
  except: pass

  # Show the class attributes of the value.
  opening_name = colored.stylize("dict: ", colored.bg("dark_cyan"))
  closing_name = colored.stylize(" :dict", colored.bg("dark_cyan"))
  try: print(f'  {opening_name}{value.__dict__}{closing_name}')
  except: pass

  # Show the value itself.
  opening_name = colored.stylize("value: ", colored.bg("dark_cyan"))
  closing_name = colored.stylize(" :value", colored.bg("dark_cyan"))
  try: print(f'  {opening_name}{value}{closing_name}')
  except: pass

import pdb
def breakpoint():
  pdb.set_trace()
