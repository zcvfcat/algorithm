# 맞는지 모름
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
    
    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        if not self.head:
            return 'LinkedList: Empty'
        
        current_node = self.head
        ll_string = 'LinkedList: '
        
        while current_node:
            ll_string += f'({str(current_node)}) -> '
            current_node = current_node.next_node
        
        ll_string += 'None'
        return ll_string
    
    def add_to_head(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

def mark_compact_algorithm(root):
    visited_nodes = set()
    stack = [root]
    
    while stack:
        current_node = stack.pop()
        
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            
            if current_node.next_node:
                stack.append(current_node.next_node)
    
    return visited_nodes


# 빈 링크드 리스트 생성
ll = LinkedList()

# 링크드 리스트에 값 추가
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(1)

# mark and compact algorithm 실행
valid_nodes = mark_compact_algorithm(ll.head)

# 결과 출력
print(valid_nodes)