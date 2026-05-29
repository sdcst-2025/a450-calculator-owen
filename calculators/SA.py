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
        'formula': lambda radius: 4*pi*(radius)**2
    },
    'cylinder': {
        'vars':['radius', 'height'],
        'formula': lambda radius, height: 2*pi*radius*(radius + height) 
    },
    'cone': {
        'vars':['radius', 'height'],
        'formula': lambda radius, height: pi*radius*(radius + (math.sqrt(radius**2 + height **2)))
    },
    'sqPyramid' : {
        'vars':['side_length', 'height'],
        'formula': lambda side_length, height: side_length * (side_length + math.sqrt(side_length**2 + 4*(height**2)))
    }
}

def SA():
    while True:
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
        print('')
        if calculatorChoice == 'end':
            break
        elif calculatorChoice in SAformulas:
            variables=[]
            for i in SAformulas[calculatorChoice]['vars']:
                globals()[i] = int(input(f'{i} = '))
                variables.append(globals()[i])
            print('')
            print('total surface area:',SAformulas[calculatorChoice]['formula'](*variables))
        elif calculatorChoice not in SAformulas:
            print('That calculator does not exist. Make sure your spelling is correct.')
        print('enter END to exit')
        time.sleep(1)
    
#print(SAformulas['cuboid']['formula'])

if __name__ == '__main__':
    SA()
