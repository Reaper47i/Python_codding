class bstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # adding child Elements
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bstNode(data)
        else:
            #add in right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bstNode(data)
