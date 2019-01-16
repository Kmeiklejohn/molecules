#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Docstring
"""

__author__ = "Kyle Meiklejohn and TJ Hindman"

import itertools


def find_dimesions(x):
    #number_range = range(1, int(x + 1))
    #cords = list(itertools.combinations_with_replacement(number_range,2))
    #cords.reverse()
    #print cords

    cords = [(w, h) for w in range(2, 11) for h in range(w, 11)]
    cords.sort(key=lambda x : x[0] * x[1], reverse=True)
    print cords
    return cords

def best_molecule(cords, across1, across2, down1, down2):
    for w, h in cords:
        w, h
    
    for a1 in range(1, 12 - w):
        for d1 in range(1, 12 - h):
            if across1[a1] != down1[d1]:
                continue
            for a2 in range(1, 12 - w):
                if across2[a2] != down2[d1+h]:
                    continue    

def main():
    molecules = ["O I M D I H E I A F N L",
                "C H J D B J M H P J K D",
                "L C B J O J G I E K B O",
                "K A I N L H L O L B E J"]

    cords = find_dimesions(10)
    
    
    best_molecule(cords, molecules[0],molecules[2],molecules[1],molecules[3])
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()