from import_graphs import convert_txt_graph_into_dict, display_matrix_graph
from floyd_algorithm import floyd_wharshall_algorithm, detect_absorbing_circuit, find_shortest_path, detect_self_cycle
import io
import sys

def choose_a_graph():
    user_choice = int(input("Enter a number between 1 and 13 to choose a graph : "))
    return user_choice


def capture_print(func, *args):
    buffer = io.StringIO()          #To keep in memory the prints
    sys.stdout = buffer             #Redirect the prints to the buffer file
    func(*args)                     #To get the prints by executing the target function
    sys.stdout = sys.__stdout__     #Stop the redirect
    return buffer.getvalue()        #put it in the file


def save_results(graph_n, path, start, end, mat_L, has_absorbing, matrix_output, floyd_output):
    filename = "result_graph_" + str(graph_n) + ".txt"
    with open(filename, "w", encoding="utf-8") as f:            #bcs inf symbole doesn't work w/ txt
        f.write("Graph " + str(graph_n) + "\n\n")

        f.write("Adjacency Matrix\n")
        f.write(matrix_output + "\n")

        f.write("Floyd-Warshall Steps\n")
        f.write(floyd_output + "\n")

        f.write("Result\n")
        if has_absorbing:
            f.write("Absorbing circuit detected. No shortest path computed.\n")
        
        else:
            f.write("Shortest path from " + str(start) + " to " + str(end) + ": " + " -> ".join(map(str, path)) + "\n")
            cost = mat_L[start][end]
            f.write("Total cost: " + str(cost) + "\n")

    print("Saved in " + filename)


def display_menu():
    graph_index = choose_a_graph()

    if graph_index < 1 or graph_index > 13:
        display_menu()
        return

    graph = convert_txt_graph_into_dict(graph_index)

    matrix_output = capture_print(display_matrix_graph, graph)
    print(matrix_output)

    floyd_output = capture_print(floyd_wharshall_algorithm, graph)
    mat_L, mat_P = floyd_wharshall_algorithm(graph)

    if detect_absorbing_circuit(mat_L):
        print("Absorbing circuit detected. No solution.")
        save_results(graph_index, [], None, None, mat_L, True, matrix_output, floyd_output)

    else:
        print("Let's calculate the shortest path between two vertices !!!!!!!!!!!!!!!!!!!!!!")
        user_start_vertex = int(input("Choose a starting vertex : "))
        user_end_vertex = int(input("Choose an ending vertex : "))

        if mat_L[user_start_vertex][user_end_vertex] >= 1e8:
            print("No path exists between " + str(user_start_vertex) + " and " + str(user_end_vertex))

        else:
            path = find_shortest_path(mat_P, user_start_vertex, user_end_vertex)
            print("Shortest path : " + " -> ".join(map(str, path)))
            print("Total cost : " + str(mat_L[user_start_vertex][user_end_vertex]))
            save_results(graph_index, path, user_start_vertex, user_end_vertex, mat_L, False, matrix_output, floyd_output)

    yes_answer = ['y', 'yes', 'oui', 'si', 'da']
    no_answer = ['n', 'no', 'non', 'niet']
    redo_algo = input("Do you want to try again with another graph ? (Y/N) : ")
    
    if redo_algo.lower() in no_answer:
        print("Okie Dockie my little cookie. Have a nice day and don't kill anybody at school *Mwaaaa*")
        exit()
    
    elif redo_algo.lower() in yes_answer:
        display_menu()
    
    else:
        exit()


display_menu()