# Just a developer tool: to generate a more detailed trace of the Python script.
import inspect
def info(value):

  # Get the expression, via which 'value' is brought here.
  # How is the value expressed in the Python language?
  frame = inspect.currentframe()
  expressions = inspect.getframeinfo(frame.f_back).code_context
  expression = expressions[0]
  left_index = expression.find('(') + 1 # jump over the opening parenthesis
  right_index = -2 # the ')\n' symbols are at the last 2 positions of the string
  expression = expression[left_index:right_index]

  # Show the given expression of the value, the value itself and the type of the value itself.
  try:
    print(f'{expression}({type(value)}, len={len(value)}, first_element_type={type(value[0])}, dir={dir(value)}, dict={value.__dict__}): {value}')
  except:
    print(f'{expression}({type(value)}): {value}')

import pdb
def breakpoint():
  pdb.set_trace()
