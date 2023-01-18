# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import importlib # dynamic import

import sol1018

def load_module(module_number):
    mod = importlib.import_module("sol"+str(module_number))
    return mod

#Do not Edit this code!
if __name__ == '__main__':

    #######################
    solution_number = 1018 # input solution number
    #######################
    # getattr(load_module(solution_number), f'sol{str(solution_number)}')()
    getattr(load_module(solution_number), f'solution')()






