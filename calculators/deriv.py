#!python3

from math import pi
from math import e

'''
--------------------------------
Avilable Functions:
    +
    -
    /
    *
    ^
-------------------------------- 
'''
#3.141 592 653 589 793

def formulaInterpreter(formula, variable):
    #replace strings with math stuff
    formatted = formula.replace('x',variable) 
    formatted = formatted.replace('^','**')
    final = eval(formatted) #evaluate formula
    return final


def deriv():
    print('derivative')
    print('enter a formula and x-value to take the derivative at a point.')
    print('note: x must be used as the variable in your equation')
    print('[formula], [x-value]')
    inputFormula = input().split(',')
    formula = inputFormula[0].lower()
    variable = inputFormula[1]
    highVariable = int(variable) + 0.000000000000001
    highVariable = str(highVariable)
    high = formulaInterpreter(formula, highVariable)
    unchanged = formulaInterpreter(formula, variable)
    derivative = (high - unchanged)/0.000000000000001
    print(derivative)

# find slightly higher secant and slightly lower secant
#(f(x+h) - f(x))/h
#

if __name__ == '__main__':
    deriv()

