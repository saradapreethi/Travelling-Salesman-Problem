################################## 
# Traveling Salesman Problem
# @author: Sarada Chandrasekar
##################################

from sys import maxsize 
from itertools import permutations
from collections import defaultdict
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt
 
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s, V): 
 
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
         
    return min_path 
 
# Driver Code 
if __name__ == "__main__": 
 
    # matrix representation of graph 
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]] 
    s = 0
    #a)Calculate the fastest route to visit all nodes for the defined graph with 4 nodes. 
    #b)Add a node to the graph and calculate the fastest route to visit all nodes.
    #c)Delete a node from the graph and calculate the fastest route to visit all nodes.
    user_input=input("Which operation to be performed?\nPlease enter option 'a' or 'b' or 'c' :\na)Calculate the fastest route to visit all nodes for the given base graph.\nb)Add a node to the graph and calculate the fastest route to visit all nodes.\nc)Delete a node from the graph and calculate the fastest route to visit all nodes.\n")
    
    #Calculate the fastest route to visit all nodes for the given base graph
    if(user_input == "a"):
        V = 4
        min_path=travellingSalesmanProblem(graph, s, V)
        print("Fastest route distance:",min_path)
        # Plot the base graph
        G = nx.from_numpy_matrix(np.array(graph))
        pos=nx.spring_layout(G)  
        nx.draw(G,pos, with_labels=True) 
        nx.draw_networkx_edge_labels(G,pos)
        plt.show()
        # Check with user whether to exit the program after execution
        input("Exit the program?")
    
    #Add a new node to the graph and calculate the fastest route to visit all nodes
    if(user_input == "b"): 
        V = 5
        # Convert the 2D graph to list
        adjList = defaultdict(list) 
        wtList = defaultdict(list)
        #Store the connected nodes in adjList and weight in WtList
        for i in range(len(graph)): 
            for j in range(len(graph[i])): 
                       if graph[i][j]!= 0: 
                           adjList[i].append(j) 
                           wtList[i].append(graph[i][j])
        
        # Fetch the weight inputs of new node from the user
        print("Enter the weights of new node:\nHint-Base graph already contains 4 nodes.New node should contain the distance to all nodes.\n")
        new_node = [int(weight) for weight in input().split()] 
       
        # Check if the user input contains distances to all nodes existing in the graph
        if(len(new_node) != 5):
            print("Warning : New node must have 5 input weights")
            print("Enter the weights of new node:")
            new_node = [int(weight) for weight in input().split()]
       
        # Add the distance of new node to adjacent list and weight list
        for i in range(len(new_node)-1):
            wtList[i].append(new_node[i])
            wtList[4].append(new_node[i])
            if(new_node[i]!=0):
                adjList[i].append(4)
                adjList[4].append(i)

        # Convert the weight list to 2D array
        wtindex=[0,1,2,3,4]
        wtarr=np.array([wtList[i] for i in wtindex])
        z=np.zeros((4,1), dtype=wtarr.dtype)
        m3=np.append(z,wtarr.reshape(4,5),1)
        wtarr=np.append(m3,0).reshape(5,5)
       
        # New graph construction: Includes the node inserted by user
        new_graph = [[0 for j in range(V)] for i in range(V)]
        for i in range(V):
            for j in adjList[i]:
                new_graph[i][j] = 1 * wtarr[i][j]
        
        #Calculate the fastest route to visit all nodes for the new graph
        min_path=travellingSalesmanProblem(new_graph, s, V)
        print("Fastest route distance for the graph with new node:",min_path)
        
        # Plot the new graph
        G = nx.from_numpy_matrix(np.array(new_graph))
        pos=nx.spring_layout(G)   
        nx.draw(G, with_labels=True) 
        nx.draw_networkx_edge_labels(G,pos)
        plt.show()

    #Delete a node from the graph and calculate the fastest route to visit all nodes.
    if(user_input == "c"): 
        nodes=[]
        # Append the available nodes in the base graph
        for i in range(len(graph)):
            nodes.append(i)
        # Display the available nodes and weights associated with each node
        print("Nodes present in the graph:",nodes)
        print("Weight/Distance of each node wrt other nodes:",graph)
        N_deletion=int(input("Please enter the node number to be deleted:"))
        # Display invalid entry if the node is not present 
        if(N_deletion > len(graph)): 
            print("Node not present!")
        # Delete the node and weights associated with it
        else:
            new_graph = np.delete(graph,N_deletion,axis=0)
            new_graph = np.delete(new_graph,N_deletion,axis=1)      
        V = len(new_graph)
        #Calculate the fastest route to visit all nodes for the new graph
        min_path=travellingSalesmanProblem(new_graph, s, V)
        print("Fastest route distance for the graph with new node:",min_path)
        if min_path != 0:
            graph = new_graph
        else:
            print("Node deletion results minimum distance = 0. Hence retaining the base graph without node deletion")
        # Plot the new graph
        G = nx.from_numpy_matrix(np.array(new_graph)) 
        pos=nx.spring_layout(G) 
        nx.draw(G, with_labels=True) 
        nx.draw_networkx_edge_labels(G,pos)
        plt.show()




    


