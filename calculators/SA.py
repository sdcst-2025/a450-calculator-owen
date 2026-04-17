#!python3
from math import pi as pi
import math

# define default states
length = 0
width = 0
height = 0
radius = 0
side_length = 0

SAformulas = {
    'cuboid': {
        'vars':[length, width, height],
        'formula': 2*(length*width + length*height + width*height)
    }, 
    'sphere': {
        'vars':[radius],
        'formula': 4 * pi * (radius)**2
    },
    'cylinder': {
        'vars':[radius, height],
        'formula': 2 * pi * radius * (radius + height)
    },
    'cone': {
        'vars':[radius, height],
        'formula': pi * radius * (radius + (math.sqrt(radius**2 + height**2)))
    },
    'sqPyramid' : {
        'vars':[side_length, height],
        'formula': side_length * (side_length + math.sqrt(side_length**2 + 4*(height**2)))
    }
}

def SA():
    print('surface area calculator')
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
    calculatorChoice = input().upper()
    if calculatorChoice == 'CUBOID': 
        variables = SAformulas['cuboid']['vars']
        for i in variables:
            pass
    if calculatorChoice == 'SPHERE':
        pass
    if calculatorChoice == 'CYLINDER':
        pass
    if calculatorChoice == 'CONE':
        pass
    if calculatorChoice == 'PYRAMID':
        pass

#print(SAformulas['cuboid']['formula'])

