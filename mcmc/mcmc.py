from copy import deepcopy
import math
import networkx as nx
import graphviz as gz
import numpy as np
#import sys
import os
class MarkovChain:
    input_f='./IOFiles/input.txt'
    G1=nx.Graph()
    iterations=20#Number of Steps in the simulation
    
    def main(self):
        self.input_arg(self.input_f)
        self.make_init_graph()
        print(len(self.M))
        bridge_selection=0
        diff_g=0
        for i in range(self.iterations):#Propose graph  modification at each simulation step
            print(self.G1.number_of_edges())
            #print("qji",self.calculate_q(self.G1))
            flag=-1
            
            while(flag==-1):#if  the randomly selected edge is a bridge select a different edge
                #print(self.G2.number_of_edges())
                A=np.random.choice(len(self.M), 2,replace=0)#Choose a tuple randomly without replacement from the range of indices in M
                flag=self.graph_change(A[0],A[1])#graph_change  function returns -1 if the edge  is  a bridge 
                #print(self.G2.number_of_edges())
                bridge_selection+=1
            if self.G1!=self.G2:#Some messages  to  show that  we have  a new connected graph
                diff_g+=1
                print("Is G2 connectes?",nx.is_connected(self.G2))
                print("G1 is not equal to G2")
            print("qij/qji",self.calculate_q(self.G2)/self.calculate_q(self.G1))
            #print(self.G1.number_of_edges())
            self.G1=deepcopy(self.G2)#As of now I am always  accepting the new graph 
        print('No. of bridges selected',bridge_selection-self.iterations)
        return(diff_g)
    
    #Function to calculate the weight of an edge            
    def dist(self,a,b):
        if type(a)==tuple and type(b)==tuple:
            wt=math.sqrt((a[1]-b[1])**2+(a[0]-b[0])**2)
            return(wt)

        else:
            print ("Inputs should be tuples")
            raise TypeError

    #Fuction for Reading the input file and storing the nodes as a list of tuples     
    def input_arg(self, in_file):
        self.M=[]
        if os.path.exists(in_file)!= True:
            print ("The input file path does not exist. Default values will be used")
            raise IOError
        f = open(in_file)

        for line in f:
            li=line.strip()
   
            if not li.startswith("#"):
                tmp = line.split(",")
                self.M.append((float(tmp[0]), float(tmp[1])))
        #print(self.M)
        f.close()
    
    #Function to  make the initial graph with the given  nodes
    def make_init_graph(self):
        
        self.G1.add_nodes_from(self.M)
        for i in range(1,len(self.M)):
            #print (i)
            self.G1.add_edge(self.M[0],self.M[i],weight=self.dist(self.M[0],self.M[i]))
        #print(self.G1.number_of_edges())
    #Function to change the state of the edge between the given nodes
    def graph_change(self,idx1,idx2):
        self.G2=deepcopy(self.G1)
        #A=np.random.choice(len(self.M), 2,replace=0)
        v1=self.M[idx1]
        v2=self.M[idx2]
        #print(v1,v2)
        if self.G2.has_edge(v1,v2)==False:
            #print(self.G1.number_of_edges())
            self.G2.add_edge(v1,v2,weight=self.dist(v1,v2))
            print("Edge has been added")
            #print(self.G2.number_of_edges())
            return(1)
        else:
            if len(nx.minimum_edge_cut(self.G2,v1,v2))==1:
                print("Is a bridge")
                A=np.random.choice(len(self.M), 2,replace=0)
                idx1=A[0]
                return(-1)
            else:
                self.G2.remove_edge(v1,v2)
                print("Edge has been removed")
                return(0)

    #Function to calculate the number of bridges in a given graph
    def calculate_bridges(self,G):
        if type(G)!=nx.Graph:
            print ("Argument passed to the function should be a Graph")
            raise TypeError
            
        b=0
        for i in G.edges():
    
            if len(nx.minimum_edge_cut(G,i[0],i[1]))==1:
                b+=1
        return(b)
    #Function to calculate the q probabilities for the proposal distribution
    def calculate_q(self,G):
        b=self.calculate_bridges(G)
        nodes=float(G.number_of_edges())
        q=(nodes*(nodes-1)/2)-b
        return(1/q)
