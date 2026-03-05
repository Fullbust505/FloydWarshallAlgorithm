import json

def load_txt_file(n):
    """Loads the graph of the corresponding given integer

    Args:
        n (int): The index of the desired graph

    Returns:
        str: The string of the content of the file
    """
    with open(f"./graphs/graph_{n}.txt") as f :
        file = f.read()
    return file

def convert_txt_graph_into_dict(n):
    """Takes a graph freshly read from its txt parent and builds a dictionnary to contain this graph.

    Args:
        n (int): The index of the desired graph in the "graphs" folder. Its content should follow the pattern : 
        
        number_of_vertices
        number_of_arcs
        source_vertex1 destination_vertex1 weight1
        source_vertex2 destination_vertex2 weight2
        source_vertex3 destination_vertex3 weight3
        ...

    Returns:
        dict: The graph in its dictionnary form
    """
    file = load_txt_file(n)
    extracted = file.split("\n")
    n_vertices = int(extracted[0])

    extracted = extracted[2:]   # Remove the two first lines, that are not arcs
    
    graph = dict()
    for vertex in range(n_vertices) :
        graph[vertex] = dict()

    for arc in extracted :

        curr_arc = arc.split(" ")
        curr_vertex = int(curr_arc[0])
        dest_vertex = int(curr_arc[1])
        weight = int(curr_arc[2])

        graph[curr_vertex][dest_vertex] = weight
            
    return graph
        

def verify_graph(graph) :
    """Verifies if a given graph is correctly initialized, checking for type errors or missing values

    Args:
        graph (dict): The graph we want to check, imported from a file

    Raises:
        ValueError: Missing values
        TypeError: Wrong type values

    Returns:
        bool: state of the verification
    """
    try:
        for vertex in graph :       # Browsing through each vertex
            for weight in graph[vertex].values():   # Browsing through each successor of the vertex
                if weight is None :
                    raise ValueError(f"Missing weight value at vertex {vertex}")
                if type(weight) != int:
                    raise TypeError(f"Incorrect type for vertex's weight {vertex}")
                    
    except ValueError as e :
        print(f"Error: {e}")
        return False
    
    except TypeError as e:
        print(f"Error : {e}")
        return False
    # I mean, we could do other errors handling, but i think it's the strict minimum for now, it's really just for convenience

    print("All checks passed : the graph is correct")
    return True

def display_matrix_graph(graph):
    """Prints the adjacency matrix of a graph.

    Args:
        graph (dict): A graph imported from a JSON file
    """
    # Sort the vertices, in case they are not sorted
    sorted_vertices = sorted(list(graph.keys()))

    size = len(sorted_vertices)
    
    # Printing header
    print("Matrix form of the graph :")
    print("  " + " ".join(f"{i}" for i in range(size)))     # 2 extra spaces for readibility purpose

    # 2. For each vertex
    for vertex in sorted_vertices :
        curr_row = str(vertex) 
        # Check if it's empty (no successor)
        if graph[vertex] == {} :
            print(curr_row + " 0"*(size))      # times 2 because of the extra space between columns and + 2 for the additional spaces on top used for spacing
        else :
            # If it has successors (check each column), browse them one by one, to guarentee a good print on the line
            for j in range(size) :
                curr_row += " "
                if j in graph[vertex] : 
                    # Big numbers will make the table unreadable
                    if graph[vertex][j] >= 1e8 :
                        curr_row += "∞"
                    else :
                        curr_row += str(graph[vertex][j]) 
                else :
                    curr_row += "0"
            print(curr_row)


if __name__== '__main__' :
    graph_1 = convert_txt_graph_into_dict(1)

    verify_graph(graph_1)

    display_matrix_graph(graph_1)
