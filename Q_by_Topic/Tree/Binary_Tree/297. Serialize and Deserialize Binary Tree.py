# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.res = ""
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(root == None):
            self.res += "N"
            return
        
        self.res += str(root.val) + "("
        self.serialize(root.left)
        self.res += "|"
        self.serialize(root.right)
        self.res += ")"
        return self.res     


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        print("__________________________")
        if(data == "N"):
            return None
        val = data.split("(")[0]
        print(val)
        node = TreeNode(int(val))
        sub_tree = data.strip(val)
        sub_tree = sub_tree[1:-1]
        level = 0
        in_left_tree = True
        left_tree = ""
        right_tree = ""
        for char in sub_tree:
            if(char == "("):
                level += 1
            elif(char == ")"):
                level -= 1
            if(char == "|" and level == 0):
                in_left_tree = False
                continue
            if(in_left_tree):
                left_tree += char
            elif(not in_left_tree):
                right_tree += char
        print(left_tree, "|", right_tree)
        
        node.left = self.deserialize(left_tree)
        node.right = self.deserialize(right_tree)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
