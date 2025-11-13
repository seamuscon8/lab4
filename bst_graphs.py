import sys
import unittest
from typing import *
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
import math 

import random
import time
from bst import *

TREES_PER_RUN : int = 10000

#Based on number n makes a BST of size n with random int values
def random_tree(n: int)->BSTree:
    def comes_before(val1: float,val2: float)->bool:
        if(val1 < val2 ):
            return True
        return False
    tree = BSTree(None,comes_before)
    for _ in range(n):
        tree = insert(tree,random.random())
    return tree

#Finds height of a  binary tree
def height(tree: BinTree)-> int:
    if(tree == None):
        return 0
    a = height(tree.left)
    b= height(tree.right)
    return 1 + max(a,b)
    
#Takes number of values, n, finds average height of tree of n values for 10,000 trees
def time_height(n: int)->float:
        h = 0
       
        for _ in range(TREES_PER_RUN):
            tree = random_tree(n)
            h = h + height(tree.bTree)
        
        return (h/TREES_PER_RUN)
        
#Takes number of values n,returns average time to insert random value into tree of size n
def time_insert(n: int)->float:
    timeTaken = 0.0
    for _ in range(TREES_PER_RUN):
        
        tree = random_tree(n)
        start = time.time()
        treeIns = insert(tree, random.random())
        end = time.time()
        timeTaken = timeTaken + (end - start)
    return timeTaken / TREES_PER_RUN


#Graphs relationship between n number of values in a tree and height of the tree
def graph1_creation() -> None:
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[int] = [ i for i in range( 0,200,4 ) ]
    y_coords : List[float] = [ time_height( x ) for x in x_coords ]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy)
    plt.xlabel("N size")
    plt.ylabel("Average Tree Height")
    plt.title("Average Tree Height of tree with N values")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()
   

#Graphs relationship between n number of values in a tree and time it takes to insert a random value
def graph2_creation() -> None:
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[int] = [ i for i in range( 0, 80 ) ]
    y_coords : List[float] = [ time_insert( x ) for x in x_coords ]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy)
    plt.xlabel("N number of values in the tree")
    plt.ylabel("Time to insert a random value into an average tree of size N")
    plt.title("Insertion time of random value vs N number of values in the tree")
    plt.grid(True)
   
    plt.show()
   
    
        
        
        

        

if(__name__ == '__main__'):
    graph2_creation()