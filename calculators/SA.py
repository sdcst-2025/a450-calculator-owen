#!python3
from math import pi as pi
import math
import time

# define default states
# numbers do not matter, different ones are used to tell what is what
'''length = 1
width = 2
height = 3
radius = 4
side_length = 5
'''
SAformulas = {
    'cuboid': {
        'vars':['length', 'width', 'height'],
        'formula': lambda length, width, height: 2*(length*width + length*height + width*height)
    }, 
    'sphere': {
        'vars':['radius'],
        'formula': '4 * pi * (radius)**2'
    },
    'cylinder': {
        'vars':['radius', 'height'],
        'formula': '2 * pi * radius * (radius + height)'
    },
    'cone': {
        'vars':['radius', 'height'],
        'formula': 'pi * radius * (radius + (math.sqrt(radius**2 + height**2)))'
    },
    'sqPyramid' : {
        'vars':['side_length', 'height'],
        'formula': 'side_length * (side_length + math.sqrt(side_length**2 + 4*(height**2)))'
    }
}

def SA():
    print('Surface Area Calculator')
    time.sleep(1)
    print('''
--------------------------------------
    what do you want to calculate?
    available calculators:
          cuboid
          sphere
          cylinder
          cone
          pyramid
--------------------------------------
''')
    calculatorChoice = input().lower()
    if calculatorChoice == 'END':
        pass
    elif calculatorChoice in SAformulas:
        for i in SAformulas[calculatorChoice]['vars']:
            globals()[i] = input(f'{i} = ')
        print(SAformulas[calculatorChoice]['formula']())
       # formulaEval = eval(SAformulas[calculatorChoice]['formula']) # needs to evaluate variables as numbers instead of strings
    elif calculatorChoice not in SAformulas:
        print('That calculator does not exist.')
        time.sleep(1)
        SA()

#print(SAformulas['cuboid']['formula'])

if __name__ == '__main__':
    SA()
