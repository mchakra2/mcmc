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
    G2=nx.Graph()
    iterations=200#Number of Steps in the simulation
    T=1
    r=1
    uniques={}#Empty dictionary to keep track of unique graphs and number of times they are observed
    def main(self):
        
        self.G1.clear()
        self.G2.clear()
        self.input_arg(self.input_f)
        self.make_init_graph()
        self.uniques.clear()
        self.mc_chain_generator()
        d0=float(self.exp_d0)/self.iterations
        E=float(self.exp_edgs)/self.iterations
        avg_path=float(self.exp_max_path)/self.iterations
        print('The expected number of edges connected to vertex 0 is ',d0)
        print('The expected number of edges in the entire graph ',E)
        print('The expected maximum distance of the shortest path in a graph that connects vertex 0 to another vertex',avg_path)
        print('The number of unique graphs ',len(self.uniques))
        #print('No. of bridges selected',bridge_selection-self.iterations)
        return(d0,E,avg_path)
    
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
                if "=" in li:
                        if  li.split("=")[0]=='T':
                            self.T=float(li.split("=")[1])
                            #print(self.T)
                        elif li.split("=")[0]=='r':
                            
                            self.r=float(li.split("=")[1])
                            print(self.r)

                else:
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
    #Function to calculate the q(m|n)  probabilitie by taking in Xn as argument
    def calculate_q(self,G):
        b=self.calculate_bridges(G)
        nodes=float(G.number_of_nodes())
        q=(nodes*(nodes-1)/2)-b
        return(1/q)

    #Funtion to return theta(Xi)
    def theta_func(self,G):
        theta=self.r*G.size(weight='weight')
        for i in range(1,G.number_of_nodes()):
            theta+=nx.shortest_path_length(G,source=G.nodes()[0],target=G.nodes()[i],weight='weight')

        return(theta)

    #Function to implement metropolis-hastings algorithm
    def MH(self):
        #f=f(Xi,Xj)=pi_j/pi_i
        f=math.exp(-float(self.theta_func(self.G2)-self.theta_func(self.G1))/self.T)
        #print(f)
        #q=q(i|j)/q(j|i)

        q=self.calculate_q(self.G2)/self.calculate_q(self.G1)
        aij=min(f*q,1)
        U=np.random.random()
        if aij>=U:
            return(1)
        else:
            return(0)

    #Function to return the maximum of the shortest path from vertex 0 to other vertices
    def max_shortest_path(self,G):
        v0=G.nodes()
        P=nx.shortest_path_length(G, source=self.M[0],weight='weight')
        max_path=-1
        for i in P:
            max_path=max(max_path,P[i])
        return(max_path)

    #Function to count uniques
    def graph_count(self,G):
        key=frozenset(G.edges(nbunch=self.M))

        if key in self.uniques:#increment count if G has been observed before
            self.uniques[key]+=1
        else:#add to the dictionary if G has not been observed before
            self.uniques[key]=1

    #Function to generate the markov chain
    def mc_chain_generator(self):
        diff_g=0
        self.uniques.clear()
        self.exp_d0=0#Expectation of degree of vertex 0
        self.exp_edgs=0
        self.exp_max_path=0
        for i in range(self.iterations):#Propose graph  modification at each simulation step
            flag=-1
            while(flag==-1):#if  the randomly selected edge is a bridge select a different edge

                A=np.random.choice(len(self.M), 2,replace=0)#Choose a tuple randomly without replacement from the range of indices in M
                flag=self.graph_change(A[0],A[1])#graph_change  function returns -1 if the edge  is  a bridge 

                            
            accept=self.MH()
            if accept==1:
                print('Change accepted')
                self.G1=deepcopy(self.G2)


            self.exp_d0+=self.G1.degree(self.M[0])
            self.exp_edgs+=self.G1.number_of_edges()
            self.exp_max_path+=self.max_shortest_path(self.G1)
            self.graph_count(self.G1)

        print(len(self.uniques))

        
