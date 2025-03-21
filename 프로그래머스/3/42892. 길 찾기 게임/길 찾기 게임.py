from collections import deque

# Node정의
class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info, self.num, self.left, self.right = info, num, left, right
        
    def has_right(self):
        return self.right is not None
    
    def has_left(self):
        return self.left is not None
    
# BT making func

def make_BT(nodeinfo):
    # 자연수로 노드 만들고
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    
    # Y좌표 내림차순, X좌표 오름차순 으로 노드 번호를 정렬 ** 배워가야 할 점
    nodes.sort(key=lambda x: (nodeinfo[x-1][1], -nodeinfo[x-1][0]), reverse=True)
    
    root = None
    for i in range(len(nodes)):
        # 루트 찾고
        if root is None:
            root = Node(nodeinfo[nodes[0]-1], nodes[0])
            
        else:
            parent = root
            node = Node(nodeinfo[nodes[i]-1], nodes[i])
            
            while True:
                # 부모 노드의 X 좌표 크기 비교 / 왼
                if node.info[0] < parent.info[0]:
                    if parent.has_left():
                        parent = parent.left
                        continue
                    parent.left = node
                    break

                # 부모노드 X 좌표 커서 오른쪽
                else:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    return root
    
def pre_order(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        # why
        if node is None:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)

def post_order(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

def solution(nodeinfo):
    answer = [[], []]
    root = make_BT(nodeinfo)
    # ? 매개변수로 주고 리턴 안받아도 업데이트가 된다. -> mutable객체 내부수정 메서드에 한해서 가능 
    pre_order(root, answer) 
    post_order(root, answer) 
    return answer