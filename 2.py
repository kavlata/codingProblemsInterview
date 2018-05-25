class BTNode:

    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None

class Tree:

    def __init__(self,val):
        self.root=BTNode(val)

    def setNext(self):
        node=self.root
        if not node.left and not node.right:
            # print(node.val)
            return node
        currentLeftNode=self.setNext1(node.left,False)
        # print(node.val)
        currentLeftNode.next = node
        currentRightNode = self.setNext1(node.right, True)
        node.next = currentRightNode
        return currentRightNode

    def setNext1(self,node, flag):
        if not node.left and not node.right:
            # print(node.val)
            return node
        currentLeftNode=self.setNext1(node.left, flag)
        # print(node.val)
        currentLeftNode.next=node
        currentRightNode=self.setNext1(node.right, flag)
        node.next=currentRightNode
        if flag:
            return currentLeftNode
        return currentRightNode

    def getItr(self):
        begin = self.root
        while begin.left:
            begin = begin.left
        return begin

l = Tree(4)
l.root.left=BTNode(2)
l.root.left.left=BTNode(1)
l.root.left.right=BTNode(3)
# l.root.left.next=l.root.left.right
# l.root.left.left.next=l.root.left
# l.root.left.right.next=l.root
l.root.right=BTNode(6)
l.root.right.left=BTNode(5)
l.root.right.right=BTNode(8)
# l.root.next=l.root.right.left
# l.root.right.left.next=l.root.right
# l.root.right.next=l.root.right.right
# l.root.right.right.next=None
l.root.right.right.left=BTNode(7)
l.root.right.right.right=BTNode(9)

# l1=l.root.left.left
# while l1.next is not None:
#    print(l1.val)
#    l1=l1.next
# print(l1.val)

l.setNext()
node1=l.getItr()
while node1.next:
    print(node1.val)
    node1=node1.next
print(node1.val)
