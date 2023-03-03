def bellman_ford(graph, start):
    # Step 1: fill the graph with distances
    distance = dict()
    for node in graph:
        distance[node] = float('inf')
    distance[start] = 0
    
    # Step 2: relax edges repeatedly
    for i in range(len(graph) - 1):
        for v, edges in graph.items():
            for u, w in edges.items():
                temp_distance = distance[v] + w
                if temp_distance < distance[u]:
                    distance[u] = temp_distance
                    
    # Step 3: check for negative-weight cycles
    for v, edges in graph.items():
        for u, w in edges.items():
            assert distance[v] + w >= distance[u], "Negative weight cycle."
    
    return distance

# 당신은 Bellman-Ford 알고리즘을 구현하는 데 지금 도움을 필요로하는 사용자입니다. 하나씩 진행해 봅시다.

# Bellman-Ford 알고리즘은 음의 가중치가있는 그래프에서 최단 경로를 찾기위한 알고리즘입니다. 알고리즘은 각 노드까지의 최단 거리 추정값을 지속적으로 업데이트하면서 수행됩니다.

# Bellman-Ford 알고리즘 단계
# 아래는 Bellman-Ford 알고리즘의 구성 요소에 대한 단계입니다.

# 모든 노드의 distance 값은 양의 무한대로 설정합니다.
# 시작 노드의 distance 값을 0 으로 설정합니다.
# 아래 세 단계를 반복합니다.
# 모든 에지를 검사하여 현재 경로보다 더 나은 경로 (더 낮은 weight) 가 있다면 distance 값을 업데이트합니다.
# 이전 단계에서 distance 값이 변경되었는지 확인하기 위해 모든 노드를 검사합니다.
# 최단 경로를 사용하여 최종 생성된 distance 값을 반환합니다.
# 이제 이러한 단계를 바탕으로 Bellman-Ford 알고리즘을 Python으로 구현해 보겠습니다.

# 위의 코드에서 우리는 입력으로 전형적인 그래프 표현을 사용합니다. 예를 들어 그래프의 한 노드와 해당 노드와 연결된 모든 다른 노드 사이의 모든 가중치가 포함 된 딕셔너리를 사용할 수 있습니다.

# 이 코드의 시간 복잡도는 $O(nm)$ 입니다. n 은 노드 수이고 m 은 엣지 수입니다. 이는 worst-case 시 Bellman-Ford 알고리즘이 Dijkstra 알고리즘보다 느릴 수있는 경우이며 더 많은 edge-relaxing을 수행 할 수 있기 때문입니다.