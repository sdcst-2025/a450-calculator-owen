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
    e
    pi
-------------------------------- 
'''

def formulaInterpreter(formula, variable):
    formatted = formula.replace('x',variable) 
    formatted = formatted.replace('^','**')
    #eval() formula



def deriv():
    print('derivative')
    print('enter a formula and x-value to take the derivative at a point.')
    print('note: x must be used as the variable in your equation')
    print('[formula], [x-value]')
    inputFormula = input().split(',')
    formula = inputFormula[0].lower()
    variable = inputFormula[1]


# find slightly higher secant and slightly lower secant
#(f(x+h) - f(x))/h
#

if __name__ == '__main__':
    deriv()