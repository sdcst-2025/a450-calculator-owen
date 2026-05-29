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
    print('derivative calculator')
    print('enter a formula and x-value to take the derivative at a point.')
    print('note: x must be used as the variable in your equation')
    print('[formula], [x-value]\n')
    inputFormula = input().split(',')
    formula = inputFormula[0].lower()
    variable = inputFormula[1]
    highVariable = str(int(variable) + 1e-15)
    lowVariable = str(int(variable) - 1e-15)
    high = formulaInterpreter(formula, highVariable)
    low = formulaInterpreter(formula, lowVariable)
    derivative = (high - low)/ (2 * 1e-15)
    print(f'\n{derivative:.5f}')
    print('Results may not be 100% accurate. Larger exponents may have larger levels of error')

    # is there a way to get a higher level of precision? it only returns 0 if the number used to change variable sizes goes any smaller
    #does it work? no. does it need to work? just round to whatever number you want. i put in a formula one time and it was 12% too big.

# using the symmetric difference quotient
# (f(x+h) - f(x-h)) / 2h

if __name__ == '__main__':
    deriv()

