'''
Created on Dec 5, 2012

@author: rodsur
'''
import varexamples
ShouldNotExit = True


def PrintChoice():
    print("What would you like to do?")
    print("Do an example with about 'variables'")
    print("'exit'")


while (ShouldNotExit):
    PrintChoice()
    choice = input()
    if choice.lower() == 'exit':
        break
    elif choice.lower() == 'variables':
        
        varexamples.example()
        pass
    else:
        print('Choice not valid, try again or contact programmer')
    pass