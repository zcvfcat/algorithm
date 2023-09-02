"""
    Stack (스택)
        후입선출(LIFO)

    시간 복잡도
        삽입(push): O(1)
        삭제(pop): O(1)
        탑(top): O(1)
        확인(peek): O(1)
        크기(size) 확인: O(1)

    사용 이유
        스택은 데이터를 임시로 저장하거나 추적    
        재귀 알고리즘
            임시 데이터를 저장
        함수 호출 시
            로컬 변수, 반환 주소 등을 스택에 저장하여 함수가 종료되면 복원
        깊이 우선 탐색(DFS), 백트래킹, 그리고 어떤 작업의 역추적
        후위 표기법
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # 3

print(stack.pop())   # 3
print(stack.pop())   # 2

print(stack.size())  # 1

print(stack.is_empty())  # False
