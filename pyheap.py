#!/usr/bin/python
#****************************************************************
# the simple heap module for create heap of chailds and parents.
#****************************************************************
#                publiced with BSDlisance
#			  2013
# author: revolt313(Hamid Rouhi)
#################################################################
__version__= '1.0.0'

def heap_gen(Data):
	global tree,parent
	tree=list(Data)
	while len(tree)>1:
		LeftChild=min(tree)
		index=tree.index(LeftChild)
		LeftChildIndex=list(tree[index])
		del tree[index]
		RightChild=min(tree)
		index=tree.index(RightChild)
		RightChildIndex=list(RightChild)
		del tree[index]
		parent=(LeftChildIndex[0]+RightChildIndex[0],LeftChild,RightChild)
		tree.append(parent)
	return tree[0]

