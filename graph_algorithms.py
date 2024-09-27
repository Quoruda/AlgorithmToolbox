import math

def dijkstra(graph, source):
    n_nodes = len(graph)
    routing_table = [[math.inf, math.inf] for i in range(n_nodes)] 
    visited = [False for i in range(n_nodes)]
    not_visited = n_nodes
    routing_table[source][1] = 0 
    while not_visited > 0:
        min_index = -1
        for i in range(n_nodes):
            if not visited[i]:
                if routing_table[i][1] < routing_table[min_index][1] or min_index == -1:
                    min_index = i                  
        visited[min_index] = True
        not_visited -=1
        value = routing_table[min_index][1]
        for i_neighbor in range(n_nodes):
            if(not visited[i_neighbor]):
                if graph[min_index][i_neighbor] > 0:
                    total = value+graph[min_index][i_neighbor]
                    if total < routing_table[i_neighbor][1]:
                        routing_table[i_neighbor][1] = total
                        routing_table[i_neighbor][0] = min_index
    return routing_table

def shortest_path(graph, source:int, dest:int):
    n_nodes = len(graph)
    routing_table = dijkstra(graph, source)
    point = dest
    path = [dest]
    while point != source:
        point = routing_table[point][0]
        path.append(point)
    path.reverse()    
    return path

def shortest_distance(graph, source:int, dest:int):
    routing_table = dijkstra(graph, source)
    return routing_table[dest][1]

graph = [
    #a,b,c,d,e,f,g
    [0,4,1,2,0,0,0],
    [4,0,0,1,2,1,0],
    [1,0,0,0,6,0,0],
    [2,1,0,0,0,3,0],
    [0,2,6,0,0,0,2],
    [0,1,0,3,0,0,3],
    [0,0,0,0,2,3,0]
]


if __name__ == "__main__":
    print(shortest_path(graph, 0,6))
    print(shortest_distance(graph, 0,6))
