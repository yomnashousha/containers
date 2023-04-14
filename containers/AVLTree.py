'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the
functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class
    declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all
        nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement
        '''
        if not node:
            return True
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        left = AVLTree._is_avl_satisfied(node.left)
        right = AVLTree._is_avl_satisfied(node.right)
        return left and right

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.right:
            new_root = Node(node.right.value)
            new_root.left = Node(node.value)
            new_root.right = node.right.right
            new_root.left.left = node.left
            new_root.left.right = node.right.left
            return new_root
        else:
            return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.left:
            old_root = Node(node.value)
            old_root.right = node.right
            old_root.left = node.left.right
            new_root = Node(node.left.value)
            new_root.left = node.left.left
            new_root.right = old_root
        else:
            new_root = node
        return new_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview
        of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code
        for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        HINT:
        Repeatedly call the insert method.
        '''
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        '''
        helper function
        '''
        if not node:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        balance = AVLTree._balance_factor(node)
        if balance > 1:
            if value < node.left.value:
                node = AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
        elif balance < -1:
            if value > node.right.value:
                node = AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        balance = AVLTree._balance_factor(node)
        right = AVLTree._balance_factor(node.right)
        left = AVLTree._balance_factor(node.left)
        if balance < -1:
            if right > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        elif balance > 1:
            if left < 0:
                node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        else:
            return node
