class Node:

    def __init__(self, data):
    #Nodes initializing

        self.left = None
        self.right = None
        self.data = data

    def gettingList(self):
    #Nodes Listing by layers'''
        lst = []
        curr_lvl = [self]
        while curr_lvl:
            for child in curr_lvl:
                lst.append(child.data)
            children = list()
            for n in curr_lvl:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            curr_lvl = children
        return lst

    def lstsum(self):
        '''Sum of Nodes'''

        suma = 0
        
        for el in self.gettingList():
            suma += el
        return suma


    def mean(self):
    #Finding mean of current tree
        return self.lstsum() / len(self.gettingList())


    
    def median(self):
    #Median Finding
        sortedLst = sorted(self.gettingList())
        mid = (len(sortedLst) - 1) // 2
        if len(sortedLst) % 2:
            return sortedLst[mid]
        else:
            return (sortedLst[mid] + sortedLst[mid + 1]) / 2

root = Node(5) # Top

root.left = Node(3) # Left Side
root.left.left = Node(2)
root.left.right = Node(5)

root.right = Node(7) # Right Side
root.right.left = Node(1)
root.right.right = Node(0)
root.right.right.left = Node(2)
root.right.right.right = Node(8)
root.right.right.right.right = Node(5)

print('Median is ', Node.median(root))
print('Mean is ', Node.mean(root))
print('Sum is ', Node.lstsum(root))