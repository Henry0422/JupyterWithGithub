'''
Created on Mar 30, 2016

@author: Henry
'''

import numpy as np
import matplotlib.pyplot as plt

class MyClass(object)??????:
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    a = np.arange(0,10,0.5)
    print 'Array a is:  ', a
    print
    
    b=a**2
    print 'Array b is:  ', b
    
    plt.ylabel('Squares')
    
    plt.plot(a,b)
    plt.show()
    
    
