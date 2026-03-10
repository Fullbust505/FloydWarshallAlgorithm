#Faire un menu pour le projet FloydWarshall Algorithm
#Le menu doit permettre à l'utilisateur de choisir entre différentes options, telles que :
#D'abbord choisir le graphe à utiliser (en anglais). Eg : Graph 1, Graph 2, etc. until Graph 13
#Ensuite, on affiche la matrix
#Puis on lance l'algorithme de Floyd Warshall sur le graphe choisi
#Ensuite, on indique si on a un absorbing cycle
#Si on a un absorbing cycle, on affiche un message qui dit 'Choose another graph' ou 'No solution'
#Si on n'a pas d'absorbing cycle, on demande à l'utilisateur de choisir un vertex de début et un vertex de fin
#À partir de sa réponse, on affiche le plus cours chemin entre les deux vertex choisis
#Enfin, on demande à l'utilisateur s'il veut recommencer ou quitter le programme
#Aussi on doit enregistrer les résultats dans un fichier txt

from import_graphs import convert_txt_graph_into_dict, display_matrix_graph
from floyd_algorithm import floyd_wharshall_algorithm, detect_absorbing_circuit, find_shortest_path, detect_self_cycle

def choose_a_graph():
    user_choice = int(input("Enter a number between 1 and 13 to choose a graph : "))
    return user_choice





#mat_L = the cost, mat_P = which vertex do we pass by
def save_results(graph_n, path, start, end, mat_L, has_absorbing):
    filename = "result_graph_" + str(graph_n) + ".txt"
    with open(filename, "w") as f:
        f.write("Graph " + str(graph_n) + "\n")
        if has_absorbing:
            f.write("Absorbing circuit detected. No shortest path computed.\n")
        else:
            f.write("Shortest path from " + str(start) + " to " + str(end) + ": " + " -> ".join(map(str, path)) + "\n")
            cost = mat_L[start][end]
            f.write("Total cost: " + str(cost) + "\n")
    print("Results saved in " + filename)


def display_menu():
    graph_index = choose_a_graph()

    if graph_index<1 or graph_index>13:
        display_menu()
        return

    graph = convert_txt_graph_into_dict(graph_index)

    display_matrix_graph(graph)

    mat_L, mat_P = floyd_wharshall_algorithm(graph)

    if detect_absorbing_circuit(mat_L):
        print("Absorbing circuit detected. No solution.")
        save_results(graph_index, [], None, None, mat_L, True)
    
    else:
        print("Let's calculate the shortest path between two vertices")
        user_start_vertex = int(input("Choose a starting vertex : "))
        user_end_vertex = int(input("Choose an ending vertex : "))

        if mat_L[user_start_vertex][user_end_vertex] >= 1e8:
            print("No path exists between " + str(user_start_vertex) + " and " + str(user_end_vertex))
        
        else:
            path = find_shortest_path(mat_P, user_start_vertex, user_end_vertex)
            print("Shortest path : " + " -> ".join(map(str, path)))                     #To do 1->2->7->...
            print("Total cost : " + str(mat_L[user_start_vertex][user_end_vertex]))
            save_results(graph_index, path, user_start_vertex, user_end_vertex, mat_L, False)

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