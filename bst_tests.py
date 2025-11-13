import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *
import math

@dataclass(frozen = True)
class Point2:
    x: float
    y: float


class BSTTests(unittest.TestCase):
    #Tests functions with integers values
    def test_int(self):
        #comes_before for integers, returns if val1 comes before val2
        def comes_before(val1:Any,val2:Any)->bool:
            if(val1<val2):
                return True
            return False
        
        #Test trees
        testBTree = BNode(10,
                BNode(9,
                    BNode(3,
                            None,
                            None),
                    None),
            BNode(20,
                    BNode(12,None,None)
                    ,  
                    BNode(40,None,None)))
        
        testBTreeInsert = BNode(10,
                BNode(9,
                    BNode(3,
                            None,
                            None),
                    None),
            BNode(20,
                    BNode(12,None,None)
                    ,  
                    BNode(40,None,BNode(60,None,None))))
        
        testBTreeDelete = BNode(10,
                BNode(9,
                    BNode(3,
                            None,
                            None),
                    None),
            BNode(12,
                    None
                    ,  
                    BNode(40,None,None)))

        #Test BSTrees
        testBST = BSTree(testBTree,comes_before)
        testBSTInsert = BSTree(testBTreeInsert,comes_before)
        testBSTDelete = BSTree(testBTreeDelete,comes_before)
        #Test is_empty on a BST
        self.assertEqual(is_empty(testBST),False)
        
        #Tests for functions with int btree

        #Test insert
        insert60 = insert(testBST,60)
        self.assertEqual(insert60,testBSTInsert)
        self.assertEqual(insert(testBST,10),testBST)
        self.assertEqual(insert(testBST,20),testBST)

        #Test lookup
        self.assertEqual(lookup(testBST,20),True)
        self.assertEqual(lookup(testBST,60),False)
        self.assertEqual(lookup(insert60,60),True)

        #Test Delete 
        self.assertEqual(delete(testBST,20),testBSTDelete)
        

    #Test functions with string values
    def test_string(self):
        #comes_before for strings, returns if val1 comes before val2
        def comes_before(val1:Any,val2:Any)->bool:
            if(val1.lower()<val2.lower()):
                return True
            return False
    
        #Test trees
        testBTree = BNode("nope",
                    BNode("car",
                        BNode("ark",
                                None,
                                None),
                        None),
                BNode("tap",
                        BNode("sap",None,None)
                        ,  
                        BNode("zap",None,None)))
        
        testBTreeInsert = BNode("nope",
                    BNode("car",
                        BNode("ark",
                                None,
                                None),
                        None),
                BNode("tap",
                        BNode("sap",None,None)
                        ,  
                        BNode("zap",BNode("top",None,None),None)))
        
        testBTreeDelete = BNode("car",
                    BNode("ark",
                        None,
                        None),
                BNode("tap",
                        BNode("sap",None,None)
                        ,  
                        BNode("zap",None,None)))
        
        #Test BSTrees
        testBSTree = BSTree(testBTree,comes_before)
        testBSTreeInsert = BSTree(testBTreeInsert,comes_before)
        testBSTreeDelete = BSTree(testBTreeDelete,comes_before)
       
        #Test insert
        insertTop = insert(testBSTree,"top")
        self.assertEqual(insertTop,testBSTreeInsert)

        #Test lookup
        self.assertEqual(lookup(testBSTree,"sap"),True)
        self.assertEqual(lookup(testBSTree,"sop"),False)
        self.assertEqual(lookup(insertTop,"top"),True)

        #Test delete
        self.assertEqual(delete(testBSTree,"nope"),testBSTreeDelete)
        self.assertEqual(lookup(delete(testBSTree,"zap"),"zap"),False)

    #Test functiosn with Point(x,y) values  
    def test_point(self):
        #comes_before for points, returns if val1 comes before val2
        def comes_before(val1: Point2,val2: Point2)->bool:
            val1Distance = math.sqrt(  ( val1.x * val1.x) + (val1.y * val1.y))
            val2Distance = math.sqrt(  ( val2.x * val2.x) + (val2.y * val2.y))
            if(val1Distance < val2Distance):
                return True
            return False

        #Test trees
        testBTree = BNode(Point2(3,4),
                    BNode(Point2(2,3),
                        BNode(Point2(1,1),
                                None,
                                None),
                        None),
                BNode(Point2(20,20),
                        BNode(Point2(8,7.5),None,None)
                        ,  
                        None))

        testBTreeInsert = BNode(Point2(3,4),
                    BNode(Point2(2,3),
                        BNode(Point2(1,1),
                                None,
                                None),
                        BNode(Point2(2.1,3.5),None,None)),
                BNode(Point2(20,20),
                        BNode(Point2(8,7.5),None,None)
                        ,  
                        None))
        
        testBTreeDelete = BNode(Point2(3,4),
                    BNode(Point2(2,3),
                        BNode(Point2(1,1),
                                None,
                                None),
                        None),
                BNode(Point2(20,20),
                       None
                        ,  
                        None))
        #BST trees
        testBSTree = BSTree(testBTree,comes_before)
        testBSTreeInsert = BSTree(testBTreeInsert,comes_before)
        testBSTreeDelete = BSTree(testBTreeDelete,comes_before)
        #Test insert
        insertPoint = insert(testBSTree,Point2(2.1,3.5))
        self.assertEqual(insertPoint,testBSTreeInsert)
        #Test Lookup
        self.assertEqual(lookup(testBSTree,Point2(8,7.5)),True)
        self.assertEqual(lookup(testBSTree,Point2(3,3)),False)
        self.assertEqual(lookup(insert(testBSTree,Point2(100,64) ),Point2(100,64)),True)

        #Test delete
        self.assertEqual(delete(testBSTree,Point2(8,7.5)),testBSTreeDelete)
        self.assertEqual( lookup(delete(testBSTree,Point2(20,20)),Point2(20,20)),False)


if (__name__ == '__main__'):
    unittest.main() 