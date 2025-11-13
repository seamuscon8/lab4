import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union['BNode',None]

#Regular binary tree
@dataclass(frozen = True)
class BNode:
    value: Any
    left: BinTree
    right: BinTree

#Includes binary tree and a comes_before function that dictates sorting
@dataclass(frozen = True)
class BSTree:
    bTree: BinTree
    comes_before: Callable[[Any,Any],bool]

#Checks if BST is empty returns true if it is
def is_empty(tree: BSTree)->bool:
    if(tree.bTree == None):
        return True
    return False

#Takes a BST and a value and calls a helper to allow comes_before function to be passed. 
# Returns BST with value insert in the right place
def insert(tree: BSTree, val: Any)-> BSTree:
    return BSTree(insertHelp(tree.bTree,val,tree.comes_before),tree.comes_before)

#Using BST and checkFunc inserts val in the right place in the BST
def insertHelp(tree: BinTree, val: Any, checkFunc: Callable[[Any,Any],bool] )-> BinTree:

    if(tree == None):
        return BNode(val, None,None)
    if(not(checkFunc(val,tree.value)) and not(checkFunc(tree.value,val))):
        return tree
    if(checkFunc(val,tree.value)):
        return BNode(tree.value,insertHelp(tree.left,val,checkFunc),tree.right)
    return BNode(tree.value,tree.left, insertHelp(tree.right,val,checkFunc))

#Takes BST and value calls helper which returns true is val is in BST
def lookup(tree: BSTree, val: Any)-> bool:
    return lookupHelp(tree.bTree, val,tree.comes_before)

#Uses BST and checkFunc to see if val is in BST and returns True if it is
def lookupHelp(tree: BinTree, val:Any, checkFunc: Callable[[Any,Any],bool])-> bool:
   
    if(tree == None):
        return False
    if(not(checkFunc(val, tree.value)) and not(checkFunc(tree.value,val))):
        return True
    
    if(checkFunc(val,tree.value)):
        return lookupHelp(tree.left,val,checkFunc)
    return lookupHelp(tree.right,val,checkFunc)


#Takes bst and finds largest value. Going to use to find largest value on left side
def findLargestVal(tree: BinTree )->Any:
    if(tree == None):
        return None
    if(tree.right == None):
        return tree.value
    else: 
        return findLargestVal(tree.right)

#Takes bst and deletes the largest value in the tree. Goes all the way to the right and deletes that node
def deleteLargest(tree: BinTree)-> BinTree:
    if(tree == None):
        return None
    if(tree.right == None):
        return tree.left
    newRight = deleteLargest(tree.right)
    return BNode(tree.value,tree.left,newRight)

#Takes tree and deletes the root of it and puts largest left value as new root, keeps ordering
def deleteRoot(tree: BinTree)-> BinTree:
    if(tree == None): 
        return None
    if(tree.left == None):
        return tree.right
    largestLeft = findLargestVal(tree.left)
    deleteLargestLeft = deleteLargest(tree.left)
    return BNode(largestLeft,deleteLargestLeft,tree.right)

#Takes BST calls helper and returns BST with val deleted from it
def delete(tree: BSTree, val: Any)-> BSTree:
    return BSTree(deleteHelp(tree.bTree,val,tree.comes_before),tree.comes_before)

#Takes tree and deletes value from it by calling other functions returns BST without val
def deleteHelp(tree: BinTree, val: Any, checkFunc: Callable[[Any,Any],bool])-> BinTree:
    if(tree == None):
        return None
    if(not(checkFunc(val,tree.value)) and not(checkFunc(tree.value,val))):
        return deleteRoot(tree)
    if(checkFunc(val,tree.value)):
        return BNode(tree.value,deleteHelp(tree.left,val,checkFunc),tree.right)
    return BNode(tree.value,tree.left,deleteHelp(tree.right,val,checkFunc))


