import math
import networkx as nx
import graphviz as gz
#import sys
import os
class MarkovChain:
    input_f='./IOFiles/input.txt'
    
    #def main(self):
    #   self.input_arg(self.input_f)
    def dist(self,a,b):
        if type(a)==tuple and type(b)==tuple:
            wt=math.sqrt((a[1]-b[1])**2+(a[0]-b[0])**2)
            return(wt)

        else:
            print ("Inputs should be tuples")
            raise TypeError

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
        print(self.M)
        f.close()
        #return (G)

    def make_init_graph(self):
        self.G=nx.Graph()
        self.G.add_nodes_from(self.M)
        for i in range(1,len(self.M)):
            self.G.add_edge(self.M[0],self.M[i])
        
