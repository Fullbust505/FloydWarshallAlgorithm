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

def choose_a_graph():
    print("Choose a graph to use:")
    print("1. Graph 1")
    print("2. Graph 2")
    print("3. Graph 3")
    print("4. Graph 4")
    print("5. Graph 5")
    print("6. Graph 6")
    print("7. Graph 7")
    print("8. Graph 8")
    print("9. Graph 9")
    print("10. Graph 10")
    print("11. Graph 11")
    print("12. Graph 12")
    print("13. Graph 13")
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


#def print_matrix(matrix):




def display_menu():
    """
    Mise en page ici
    """
    graph = choose_a_graph()
    graph_choice(graph)
    print_matrix(graph)
    floyd_wharshall_algorithm(graph)
    detect_self_cycle(graph)

    while detect_self_cycle(graph) == True :
        print("Choose another graph")
        display_menu()


    print("Let's calculate the shortest path between two vertex") 
    user_start_vertex = int(input("Choose a starting vertex"))
    user_end_vertex = int(input("Choose an ending vertex"))

    #insert here fonction pour le chemin le plus court (user_start_vertex, user_end_vertex)

    yes_answer = ['y', 'yes', 'oui', 'si', 'da']
    no_answer = ['n', 'no', 'non', 'niet']
    redo_algo = input("Do you want to try again with another graph ? (Y/N) : ")
    if redo_algo.lower in no_answer:
        print("Okie Dockie my little cookie. Have a nice day and don't kill anybody at school *Mwaaaa*")



display_menu()