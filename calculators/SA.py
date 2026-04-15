#!python3
from math import pi as pi
import math

def SA():
    print('surface area')

SAformulas = {
    'cuboid': {
        'vars':['length', 'width', 'height'],
        'formula': '2*(length*width + length*height + width*height)'
    }, 
    'sphere': {
        'vars':['radius'],
        'formula': '4 * pi * (radius)**2'
    },
    'cylinder': {
        'vars':['radius', 'height'],
        'formula': '2 * pi * radius * (radius + height)'
    },
    'triangularPrism': {
        'vars':[],
        'formula': pi * radius * ( )
    },
    'cone':
    'sqPyramid'
    'triPyramid'
    # πr^2 + πr√(r2 + h2)
}