from import_graphs import convert_txt_graph_into_dict, display_matrix_graph
from floyd_algorithm import floyd_wharshall_algorithm
import copy
import numpy as np

def floyd_warshall_log(matrix_rate):
    """
    Applies Floyd-Warshall algorithm but with logarithms on the values, in order to have a change of scale.
    
    Returns the matrix L (of the distances of the shortest path) 
    and a boolean confirming or denying the presence of absorbing cycles.
    """
    n = len(matrix_rate)
    
    distance_log = copy.deepcopy(graph_rates)
    for i in range(n):
        for j in range(n):
            if i == j:
                distance_log[i][j] = 0
            elif matrix_rate[i][j] > 0:
                distance_log[i][j] = -np.log(matrix_rate[i][j])
            
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance_log[i][k] + distance_log[k][j] < distance_log[i][j]:
                    distance_log[i][j] = distance_log[i][k] + distance_log[k][j]
    
    negative_cycle_presence = False
    for i in range(n):
        if distance_log[i][i] < 0:
            negative_cycle_presence = True
            break
    
    return distance_log, negative_cycle_presence

if __name__=="__main__":

    graph_rates = convert_txt_graph_into_dict(14)
    n = len(graph_rates)

    mat_L, arbit = floyd_warshall_log(graph_rates)

    display_matrix_graph(mat_L)

    print("We notice only negative cycles.")
