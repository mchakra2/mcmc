import math
import unittest
class MarkovChain:
    #def arguments(self,in_file):
    def main(self):
        self.dist((1,1),1)
    def dist(self,a,b):
        if type(a)==tuple and type(b)==tuple:
            wt=math.sqrt((a[1]-b[1])**2+(a[0]-b[0])**2)
            return(wt)

        else:
            print ("Inputs should be tuples")
            raise TypeError
