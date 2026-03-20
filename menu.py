from import_graphs import convert_txt_graph_into_dict, display_matrix_graph
from floyd_algorithm import floyd_wharshall_algorithm, detect_absorbing_circuit, find_shortest_path, detect_self_cycle
import io
import sys
import re

# Check the validity of the user input
def secure_input(txt, valid_range):
    while True:
        try:
            user_input = int(input(txt))
            if user_input in valid_range:
                return user_input
            else:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
           
def choose_a_graph():
    user_choice = secure_input("Enter a number between 1 and 14 to choose a graph : ", list(range(1, 15)))
    return user_choice

def capture_print(func, *args):
    buffer = io.StringIO()              #To keep in memory the prints
    sys.stdout = buffer                 #Redirect the prints to the buffer file
    result = func(*args)                #To get the prints by executing the target function
    sys.stdout = sys.__stdout__         #Stop the redirect
    return buffer.getvalue(), result    #put it in the file and return the result of the function

# Clean the parameter from the color codes
def strip_ansi_codes(text):
    # Remove all the code of type : \x1b[...m
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)


def save_results(graph_n, path, start, end, mat_L, has_absorbing, matrix_output, floyd_output):
    filename = "result_graph_" + str(graph_n) + ".txt"

    # Remove the color codes from the outputs
    clean_matrix = strip_ansi_codes(matrix_output)
    clean_floyd_output = strip_ansi_codes(floyd_output)

    with open(filename, "w", encoding="utf-8") as f:            # because inf symbol doesn't work with txt format
        f.write("Graph " + str(graph_n) + "\n\n")

        f.write("Adjacency Matrix\n")
        f.write(clean_matrix + "\n")

        f.write("Floyd-Warshall Steps\n")
        f.write(clean_floyd_output + "\n")

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

    if graph_index < 1 or graph_index > 14:
        display_menu()
        return

    # Loasd the graph and convert it into a dict
    graph = convert_txt_graph_into_dict(graph_index)

    # Display the graph as a matrix and capture its prints
    matrix_output, _ = capture_print(display_matrix_graph, graph)
    print(matrix_output)

    # Run the Floyd-Warshall algorithm and capture its prints
    floyd_output, (mat_L, mat_P) = capture_print(floyd_wharshall_algorithm, graph)
    print(floyd_output)

    if detect_absorbing_circuit(mat_L):
        print("Absorbing circuit detected. No solution.")
        save_results(graph_index, [], None, None, mat_L, True, matrix_output, floyd_output)

    else:
        print("Let's calculate the shortest path between two vertices !")
        user_start_vertex = secure_input("Choose a starting vertex : ", list(range(len(graph))))
        user_end_vertex = secure_input("Choose an ending vertex : ", list(range(len(graph))))

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
        print("See you soon !")
        exit()
    
    elif redo_algo.lower() in yes_answer:
        display_menu()
    
    else:
        exit()


display_menu()