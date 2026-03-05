from import_graphs import convert_txt_graph_into_dict, display_matrix_graph
import copy

def detect_self_cycle(graph):
    """Detects if vertices from a graph have an outgoing edge towards themselves

    Args:
        graph (dict): A graph to be analysed

    Returns:
        bool: confirmation or denial of the presence of a self cycle
    """
    for vertex in graph : 
        if graph[vertex] != None :
            for destination in graph[vertex].keys() :
                if destination == vertex :
                    return True
    return False


def floyd_wharshall_algorithm(graph):
    """Main function for Floyd Warshall's algorithm. 
    It first creates the matrices L and P, the later being used to track predecessors of shortest paths 
    and the former computing the shortest path from a vertex to another.

    Args:
        graph (dict): A graph to be analysed
    """
    # Copies of graph are mandatory when editing them, because regular equalities create a shallow copy (copy of a reference) and we need a deep copy (copy of the values)
    mat_L = copy.deepcopy(graph)
    mat_P = copy.deepcopy(graph)
    inf = 1e8       # 10^8, big number that can never be equalized
    n = len(graph)

    for i in range(n) :
        mat_L[i][i] = 0
        for j in range(n):
            mat_P[i][j] = i
            if j not in mat_L[i] :
                mat_L[i][j] = inf
            
    # For each intermediate vertex
    for k in range(n) :
        # For each source vertex
        for i in range(n) :
            # For each destination vertex
            for j in range(n) :
                if (mat_L[i][k] + mat_L[k][j] < mat_L[i][j]):
                    mat_L[i][j] = mat_L[i][k] + mat_L[k][j]
                    mat_P[i][j] = mat_P[k][j]

    display_matrix_graph(mat_L)
    display_matrix_graph(mat_P)

    return 

if __name__ == "__main__":
    graph_1 = convert_txt_graph_into_dict(1)
    
    floyd_wharshall_algorithm(graph_1)
    