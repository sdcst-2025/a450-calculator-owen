#!python3

from math import pi as pi
import time

areaFormulas = {
    'rectangle': {
        'vars':['length', 'width'],
        'formula': lambda length, width: length*width
    },
    'triangle': {
        'vars':['base', 'height'],
        'formula': lambda base, height : (1/2)*base*height
    },
    'circle':{
        'vars':['radius'],
        'formula': lambda radius: pi*(radius**2)
    },
    'trapezoid':{
        'vars':['side_1','side_2','height'],
        'formula': lambda side_1, side_2, height: (1/2)*(side_1 + side_2)*height
    }
}

def area():
    while True:
        print('Area Calculator')
        time.sleep(1)
        print('''
--------------------------------------
    what do you want to calculate?
    available calculators:
        rectangle
        triangle
        circle
        trapezoid 
--------------------------------------
''')
        calculatorChoice = input().lower()
        print('')
        if calculatorChoice == 'end':
            break
        elif calculatorChoice in areaFormulas:
            variables=[]
            for i in areaFormulas[calculatorChoice]['vars']:
                globals()[i] = int(input(f'{i} = '))
                variables.append(globals()[i])
            print('')
            print('Area:',areaFormulas[calculatorChoice]['formula'](*variables))
            time.sleep(1)
        elif calculatorChoice not in areaFormulas:
            print('That calculator does not exist. Make sure your spelling is correct.')
        print('enter END to exit')
        time.sleep(1)

if __name__ == '__main__':
    area()
