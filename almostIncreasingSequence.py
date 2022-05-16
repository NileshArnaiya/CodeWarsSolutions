# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:03:11 2022

@author: nILESH JAIN
"""

def checkDup(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
        
def almost_increasing_sequence(sequence):
    ogcopy = sequence.copy()
    for i in range(len(sequence)):
        ogcopy.pop(i)
        if ogcopy == sorted(ogcopy) and not checkDup(ogcopy):
            return True
        ogcopy = sequence.copy()
    return False