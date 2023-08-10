# Python Program to Insert, Search and Print an Element in a B+ Tree 

# define a class for B+ tree node 
class BPlusTreeNode(): 
	
	# Constructor to create a new Node 
	def __init__(self, keys=[], child=[], isLeaf=True, max_num_keys=5): 
		self.keys = keys 
		self.child = child 
		self.isLeaf = isLeaf 
		if max_num_keys < 3: # max_num_keys must be odd and greater or equal to 3 
			max_num_keys = 3 
		if max_num_keys % 2 == 0: # max_num_keys must be odd and greater or equal to 3 
			max_num_keys += 1 
		self.max_num_keys = max_num_keys 

# define a class for B+ tree 
class BPlusTree(): 
	
	# Constructor to create a new B+ tree 
	def __init__(self, max_num_keys=5): 
		self.root = BPlusTreeNode(max_num_keys=max_num_keys) 
		
	# search a key in the B+ tree 
	def search(self, k): 
		
		# return None if the tree is empty 
		if self.root.keys == []: 
			return None
		
		# find the node containing key k 
		node = self._find(self.root, k) 
		
		# returns the key if found 
		for i in range(len(node.keys)): 
			if k == node.keys[i]: 
				return k 
		
		# else return None 
		return None
	
	# find the node containing key k 
	def _find(self, node, k): 
		
		# if node is a leaf 
		if node.isLeaf: 
			return node 
		
		# if k is smaller than the smallest key 
		if k < node.keys[0]: 
			return self._find(node.child[0], k) 
		
		# if k is greater than or equal to the 
		# smallest key of the right most child 
		if k >= node.keys[-1]: 
			return self._find(node.child[-1], k) 
		
		# else search in the appropriate child 
		for i in range(len(node.keys)): 
			if k >= node.keys[i] and k < node.keys[i+1]: 
				return self._find(node.child[i+1], k) 
	
	# insert an element in the B+ tree 
	def insert(self, k): 
		
		# if the tree is empty 
		if self.root.keys == []: 
			self.root.keys.append(k) 
			return
		
		# if the root is full 
		if len(self.root.keys) == self.root.max_num_keys: 
			
			# create a new node to store the old nodes 
			new_node = BPlusTreeNode(max_num_keys=self.root.max_num_keys) 
			new_node.child.append(self.root) 
			self.root = new_node 
			
			# split the old root and move a key to the new root 
			self._split_child(self.root, 0, self.root.child[0]) 
		
		# insert the new key in the appropriate leaf 
		self._insert_non_full(self.root, k) 
	
	# split the child node at index i of the node 
	def _split_child(self, node, i, child): 
		
		# create a new node to store (max_num_keys//2) keys of child 
		new_node = BPlusTreeNode(max_num_keys=child.max_num_keys) 
		new_node.isLeaf = child.isLeaf
		
		# move the last (max_num_keys//2) keys of child to new_node 
		new_node.keys = child.keys[child.max_num_keys//2:] 
		
		# if child is an internal node, move the last (max_num_keys//2 + 1) 
		# children of child to new_node 
		if not child.isLeaf: 
			new_node.child = child.child[child.max_num_keys//2+1:] 
		
		# set child's number of keys to (max_num_keys//2) 
		child.keys = child.keys[:child.max_num_keys//2] 
		
		# if child is an internal node, set its number of children 
		# to (max_num_keys//2) 
		if not child.isLeaf: 
			child.child = child.child[:child.max_num_keys//2+1] 
		
		# move the middle key of child to node 
		node.keys.insert(i, child.keys.pop()) 
		
		# link new_node to node 
		node.child.insert(i+1, new_node) 
	
	# insert an element in the subtree rooted at node 
	def _insert_non_full(self, node, k): 
		
		# if node is a leaf, insert k in node 
		if node.isLeaf: 
			node.keys.append(k) 
			node.keys.sort() 
			return
		
		# else decide the appropriate child of node 
		# to move down the tree 
		i = 0
		while i < len(node.keys) and k > node.keys[i]: 
			i += 1
		
		# if the child is full 
		if len(node.child[i].keys) == node.child[i].max_num_keys: 
			
			# split the child 
			self._split_child(node, i, node.child[i]) 
			
			# decide the child node 
			# to move down the tree 
			if k > node.keys[i]: 
				i += 1
		
		# move down the tree recursively 
		self._insert_non_full(node.child[i], k) 
	
	# print the B+ tree 
	def printTree(self): 
		
		# if the tree is empty 
		if self.root.keys == []: 
			print('Empty Tree') 
			return
		
		# else call the recursive function 
		self._printTree(self.root) 
	
	# recursive function to print the tree 
	def _printTree(self, node): 
		
		# if node is a leaf, print its keys 
		if node.isLeaf: 
			for i in range(len(node.keys)-1): 
				print(node.keys[i], end=' | ') 
			print(node.keys[len(node.keys)-1], end=' ') 
			return
		
		# else call the function recursively for all its children 
		for i in range(len(node.keys)): 
			self._printTree(node.child[i]) 
			print(node.keys[i], end=' | ') 
		self._printTree(node.child[len(node.keys)]) 
		
# driver code 
tree = BPlusTree() 

# insert elements 
elements = [5, 9, 10, 0, 6, 11, -1, 1, 2] 
for i in range(len(elements)): 
	tree.insert(elements[i]) 

# print tree 
tree.printTree() 

# search for an element 
print("\nSearch for 10:", tree.search(10)) 
print("Search for 12:", tree.search(12))