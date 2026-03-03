import json

def load_txt_file(n):
    with open(f"./graphs/graph_{n}.txt") as f :
        file = f.read()
    return file

def sort_list_str(arr):
    """A sorting function for lists of strings, that returns it sorted and still as strings. 
    Defined to make the display_matrix_graph() lighter.

    Args:
        arr (list): A list or array of numbers wrapped in the string format

    Returns:
        list: The sorted list, with elements still in string format
    """
    temp_arr = list(map(int, arr))
    temp_arr.sort()
    return list(map(str, temp_arr))

def convert_txt_graph_into_dict(file):
    extracted = file.split("\n")
    n_vertices = int(extracted[0])
    n_arcs = int(extracted[1])

    extracted = extracted[2:]
    
    graph = dict()
    for vertex in range(n_vertices) :
        graph[str(vertex)] = None
    for arc in range(n_arcs) :
        curr_vertex = extracted[arc][0]
        dest_vertex = extracted[arc][2]
        weight = int(extracted[arc][4])
        if graph[curr_vertex] is None :
            graph[curr_vertex] = dict()
        graph[curr_vertex][dest_vertex] = weight
    
    return graph
        

def load_json_graph(n):
    """Loads the graph of the corresponding given integer

    Args:
        n (int): The index of the desired graph

    Returns:
        dict: The dict containing the graph
    """
    with open(f'./graphs/graph_{n}.json') as f:
        graph = json.load(f)
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
            if graph[vertex] != None :      # To avoid bumping into vertices w/o successors
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
    # 1. Sort the vertices, in case they are not sorted
    sorted_vertices = sort_list_str(list(graph.keys()))

    size = len(sorted_vertices)
    # 2. Check each vertex and print out its outgoing edges
    print("Matrix form of the graph :")
    print("  " + " ".join(f"{i}" for i in range(size)))     # 2 extra spaces for readibility purpose

    for i in range(len(sorted_vertices)) :
        vertex = sorted_vertices[i]
        if graph[vertex] == None :
            print(str(i) + " "*(2*size+2))      # times 2 because of the extra space between columns and + 2 for the additional spaces on top used for spacing
        else :
            curr_row = str(i) + " "         # number at start + extra space makes up for the 2 extra spaces used for spacing on top
            for j in range(size) :
                if str(j) in graph[vertex] : 
                    curr_row += str(graph[vertex][str(j)]) + " "
                else :
                    curr_row += "  "
            print(curr_row)


if __name__== '__main__' :
    graph_1 = load_json_graph(1)
    print(graph_1)
    
    graph_1 = load_txt_file(1)
    graph_1 = convert_txt_graph_into_dict(graph_1)


    verify_graph(graph_1)

    display_matrix_graph(graph_1)
