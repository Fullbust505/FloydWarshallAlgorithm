import json

def verify_graph(graph) :
    try :
        graph["start"] == None or graph["end"] == None 
    except :
        print("Error : No starting vector or ending vector specified")
        return False
    
    try:
        for vertex in graph["vertices"] :
            if graph["vertices"][vertex] != None :      # To avoid bumping into vertices w/o succesors   
                for weight in graph["vertices"][vertex].values():
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


if __name__== '__main__' :
    with open('./graphs/graph_1.json') as f:
        graph_1 = json.load(f)
        print(graph_1)
    
    verify_graph(graph_1)
