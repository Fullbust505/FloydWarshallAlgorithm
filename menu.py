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

def graph_choice(user_choice):
    if user_choice == 1:
        return "Graph 1"
    elif user_choice == 2:
        return "Graph 2"
    elif user_choice == 3:
        return "Graph 3"
    elif user_choice == 4:
        return "Graph 4"
    elif user_choice == 5:
        return "Graph 5"
    elif user_choice == 6:
        return "Graph 6"
    elif user_choice == 7:
        return "Graph 7"
    elif user_choice == 8:
        return "Graph 8"
    elif user_choice == 9:
        return "Graph 9"
    elif user_choice == 10:
        return "Graph 10"
    elif user_choice == 11:
        return "Graph 11"
    elif user_choice == 12:
        return "Graph 12"
    elif user_choice == 13:
        return "Graph 13"
    else:
        print("Invalid choice. Please choose a number between 1 and 13.")
        return None



def print_matrix(graph):
    n = len(graph)
    matrix = [[INF] * n for _ in range(n)]

    
    for i in range(n):
        matrix[i][i] = 0

   
    for u in graph:
        for v, weight in graph[u].items():
            matrix[u][v] = weight
            
    return matrix


def save_results(graph_n, path, start, end, mat_L, has_absorbing):
    filename = f"result_graph_{graph_n}.txt"
    with open(filename, "w") as f:
        f.write(f"Graph {graph_n}\n")
        if has_absorbing:
            f.write("Absorbing circuit detected. No shortest path computed.\n")
        else:
            f.write(f"Shortest path from {start} to {end}: {' -> '.join(map(str, path))}\n")
            cost = mat_L[start][end]
            f.write(f"Total cost: {cost}\n")
    print(f"Results saved in {filename}")

def display_menu():
    """
    Mise en page ici
    """
    graph = choose_a_graph()
    graph_nb = graph_choice(graph)
    print_matrix(graph_nb)
    floyd_wharshall_algorithm(graph_nb)
    detect_self_cycle(graph)

    while detect_self_cycle(graph) == True :
        print("Choose another graph")
        display_menu()


    print("Let's calculate the shortest path between two vertex") 
    user_start_vertex = int(input("Choose a starting vertex"))
    user_end_vertex = int(input("Choose an ending vertex"))

    find_shortest_path(mat_P, user_start_vertex, user_end_vertex)

    yes_answer = ['y', 'yes', 'oui', 'si', 'da']
    no_answer = ['n', 'no', 'non', 'niet']
    redo_algo = input("Do you want to try again with another graph ? (Y/N) : ")
    if redo_algo.lower in no_answer:
        print("Okie Dockie my little cookie. Have a nice day and don't kill anybody at school *Mwaaaa*")
        exit()
    if redo_algo.lower in yes_answer:
        display_menu()
    else :
        exit()


display_menu()


#to finish