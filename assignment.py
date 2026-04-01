#!python3
# Volume Calculator
# Feel free to rename your variables
'''
These things can include:
volume calculations *
surface area calculations *
area calculations *
calculations of derivatives *
interest calculations *
tax calculations
earnings
'''

import calculators.volume as volume
import calculators.SA as SA
import calculators.area as area
import calculators.deriv as deriv
import calculators.interest as interest

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print('''
--------------------------------
      Welcome to Calculator
          
    Enter "help" for Help
    Enter "end" to Quit Program
--------------------------------
''')
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print('''
--------------------------------
Available Commands:
    command -- keyword
    display title -- title
    volume calculator -- vol
    surface area calculator -- SA
    area calculator -- area
    derivative calculator - deriv
    interest calculator -- int
--------------------------------
''')
    return None

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        userInput = input().lower()
        if userInput == 'help': instructions()
        elif userInput == 'title': title()
        elif userInput == 'vol': volume.volume()
        elif userInput == 'sa': SA.SA()
        elif userInput == 'area': area.area()
        elif userInput == 'deriv': deriv.deriv()
        elif userInput == 'int': interest.interest()
        elif userInput == 'end': break
        pass

if __name__ == "__main__":
    main()
