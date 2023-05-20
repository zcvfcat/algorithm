class BPlusTreeNode():
    def __init__(self, keys=[], child=[], isLeaf=True, max_num_keys=5):
        self.keys = keys
        self.child = child
        self.isLeaf = isLeaf

        if max_num_keys < 3:
            max_num_keys = 3
        
        if max_num_keys % 2 == 0:
            max_num_keys += 1
        
        self.max_num_keys = max_num_keys

class BPlusTree():
    def __init__(self, max_num_keys = 5):
        self.root = BPlusTreeNode(max_num_keys=max_num_keys)
        