#!python3

from math import pi as pi
import time

volumeFormulas = {
    'cuboid': {
        'vars':['length', 'width', 'height'],
        'formula': lambda length, width, height: length*width*height
    }, 
    'sphere': {
        'vars':['radius'],
        'formula': lambda radius: (4/3)*pi*(radius**2)
    },
    'cylinder': {
        'vars':['radius', 'height'],
        'formula': lambda radius, height: pi*(radius**2)*height
    },
    'cone': {
        'vars':['radius', 'height'],
        'formula': lambda radius, height: (1/3)*pi*(radius**2)*height
    },
    'pyramid' : {
        'vars':['side_length', 'height'],
        'formula': lambda side_length, height: (1/3)*(side_length**2)*height
    }
}

def volume():
    while True:
        print('Volume Calculator')
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
        elif calculatorChoice in volumeFormulas:
            variables=[]
            for i in volumeFormulas[calculatorChoice]['vars']:
                globals()[i] = int(input(f'{i} = '))
                variables.append(globals()[i])
            print('')
            print('Volume:',volumeFormulas[calculatorChoice]['formula'](*variables))
            time.sleep(1)
        elif calculatorChoice not in volumeFormulas:
            print('That calculator does not exist. Make sure your spelling is correct.')
        print('enter END to exit')
        time.sleep(1)

if __name__ == '__main__':
    volume()
