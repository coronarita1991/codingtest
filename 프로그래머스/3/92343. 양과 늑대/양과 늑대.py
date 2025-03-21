# 트리 구조 저장
def make_tree(info, edges):
    adj_list = [[] for _ in range(len(info))]
    for i in edges:
        s, e = i
        adj_list[s].append(e)
    return adj_list

from collections import deque

def solution(info, edges):
    max_sheep = 0
            
    adj_list = make_tree(info, edges)
    
    q = deque()    
    
    # 가져 갈 항목 : sheep_count, wolf_count, node_number, visited(set)
    q.append((1, 0, 0, set()))
    
    # BFS 와 답 갱신
    while q:
        sheep_count, wolf_count, node_number, visited = q.popleft()
        # 최댓값 갱신
        max_sheep = max(max_sheep, sheep_count)
        # 다음 경로를 추가        
        visited.update(adj_list[node_number])
        
        # 다음 경로 순회
        for next_node in visited:
            # 늑대라면
            if info[next_node]:
                if sheep_count != wolf_count+1 : 
                    q.append((sheep_count, wolf_count+1, next_node, visited - {next_node}))
            # 양이라면 무조건 추가
            else:
                q.append((sheep_count+1, wolf_count, next_node, visited - {next_node}))
    
    return max_sheep