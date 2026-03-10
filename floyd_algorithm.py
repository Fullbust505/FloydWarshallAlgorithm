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

    for i in range(n):
        mat_L[i][i] = 0
        for j in range(n):
            mat_P[i][j] = i
            if j not in mat_L[i]:
                mat_L[i][j] = inf

    print("\nFIRST STEP\n")
    display_matrix_graph(mat_L)
    display_matrix_graph(mat_P)
            
    # For each intermediate vertex
    for k in range(n):
        # For each source vertex
        for i in range(n):
            # For each destination vertex
            for j in range(n):
                if mat_L[i][k] == inf or mat_L[k][j] == inf:
                    mat_L[i][j] = mat_L[i][j] #no change
                elif mat_L[i][k] + mat_L[k][j] < mat_L[i][j]:
                    mat_L[i][j] = mat_L[i][k] + mat_L[k][j]
                    mat_P[i][j] = mat_P[k][j]
        print("===============")
        print("\nNEXT STEP\n")
        display_matrix_graph(mat_L)
        display_matrix_graph(mat_P)

    print("\n===============\n")
    print("FINAL MATRICES") # the lasts matrices are printed 2 times
    display_matrix_graph(mat_L)
    display_matrix_graph(mat_P)

    return mat_L, mat_P

def detect_absorbing_circuit(mat_L):
    """

    Args:
        mat_L: the matrix we found with Floyd-Warshall algorithm storing the cost of the shortest path

    Returns:
        A boolean saying whether it detected an absorbing circuit or not

    """
    nb_lines = len(mat_L)
    for i in range(nb_lines):
        if mat_L[i][i] < 0:
            return True
    return False


def find_shortest_path(mat_P, start_vertex, end_vertex):
    """

    Args:
        mat_P: the matrix we found with Floyd-Warshall algorithm storing the predecessor for each path between 2 points
        start_vertex: begin of the path
        end_vertex: end of the path

    Returns:

    """
    shortest_path = [end_vertex]
    curr_dest_vertex = end_vertex

    while mat_P[start_vertex][curr_dest_vertex] != start_vertex:
        shortest_path.append(mat_P[start_vertex][curr_dest_vertex])
        curr_dest_vertex = mat_P[start_vertex][curr_dest_vertex]

    shortest_path.append(start_vertex) # shortest path stored but reversed
    shortest_path = shortest_path[::-1]

    return shortest_path


if __name__ == "__main__":
    graph_1 = convert_txt_graph_into_dict(1)
    graph_2 = convert_txt_graph_into_dict(2)
    current_graph = convert_txt_graph_into_dict(11)
    
    final_mat_L, final_mat_P = floyd_wharshall_algorithm(current_graph)
    bool = detect_absorbing_circuit(final_mat_L)
    #print(bool)
    path = find_shortest_path(final_mat_P, 2, 0)
    print(path)
    