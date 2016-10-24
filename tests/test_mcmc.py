#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mcmc
----------------------------------

Tests for `mcmc` module.
"""

import math
import sys
import os
import unittest
import networkx as nx
from contextlib import contextmanager
from click.testing import CliRunner
from mcmc import mcmc



class TestMcmc(unittest.TestCase):

    def setUp(self):
        #pass
        self.m=mcmc.MarkovChain()

    def tearDown(self):
        pass

    def test_dist_arg_type(self):#test if the dist function rises errors when given non numerical tuples  as input
       
        with self.assertRaises(TypeError):
            self.m.dist((-4,1),1)
        with self.assertRaises(TypeError):
            self.m.dist(2.2,'a')
        with self.assertRaises(TypeError):
            self.m.dist(('A',3),(2.2,1))



    def test_dist_return(self):#To check if dist function returns the cartesian distance between  given tuples   
        
        val=round(math.sqrt(2.2**2+2.2**2),2)
        wt=self.m.dist((2.2,2.2), (0,0))
        self.assertEqual(round(wt,2),val)
        self.assertEqual(self.m.dist((2,0),(2,0)),0)
    
    def test_input_file(self):#Test that input_arg raises error if input file does not exist and is not  empty
           
        self.assertRaises(IOError,self.m.input_arg,'random_file_which_should_not_exist.txt')
        #self.m.main()
        flag = os.path.getsize(self.m.input_f)
        self.assertGreater(flag,0)
        self.assertGreater(self.m.T,0)#makes sure that T is strictly positive

    def test_tuples(self):
        self.m.input_arg('./tests/test_input.txt')
        self.assertGreater(len(self.m.M),0)#To ensure that the number of vertices is greater than 0

    def test_make_init_graph(self):
        self.m.G1.clear()
        self.m.input_arg('./tests/test_input.txt')
        self.m.make_init_graph()
        self.assertIsInstance(self.m.G1,nx.Graph)
        self.assertTrue(nx.is_connected(self.m.G1),'Initial Graph is connected')#checks if initial graph is connected
        
        #self.assertTrue(self.m.G1.number_of_edges()==(self.m.G1.number_of_nodes() -1))


    def test_graph_change_add(self):
        self.m.input_arg('./tests/test_input.txt')
        self.m.make_init_graph()
        self.assertEqual(self.m.graph_change(1,2),1)
        self.assertNotEqual(self.m.G1.number_of_edges(),self.m.G2.number_of_edges())
        self.m.G1.clear()
        self.m.G2.clear()


    def test_graph_change_bridge(self):
        self.m.input_arg('./tests/test_input.txt')
        self.m.make_init_graph()
        self.assertEqual(self.m.graph_change(0,2),-1)
        self.assertEqual(self.m.G1.number_of_edges(),self.m.G2.number_of_edges())
        self.m.G1.clear()
        self.m.G2.clear()


    def test_graph_change_remove(self):
        self.m.input_arg('./tests/test_input.txt')
        self.m.make_init_graph()
        v1=self.m.M[1]
        v2=self.m.M[2]
        wt=self.m.dist(v1,v2)
        print(wt)
        self.m.G1.add_edge(v1,v2,weight=wt)
        self.assertEqual(self.m.graph_change(1,2),0)
        self.assertNotEqual(self.m.G1.number_of_edges(),self.m.G2.number_of_edges())
        self.m.G1.clear()
        self.m.G2.clear()


    def test_calculate_bridges(self):
        a=1
        self.assertRaises(TypeError,self.m.calculate_bridges,a)
        G=nx.cycle_graph(3)
        self.assertEqual(0,self.m.calculate_bridges(G))
        G1=nx.star_graph(5)
        self.assertEqual(5,self.m.calculate_bridges(G1))
        G1.clear()
        G.clear()

    def test_calculate_q(self):
        G1=nx.star_graph(5)
        self.assertGreater(self.m.calculate_q(G1),0)
        self.assertLess(self.m.calculate_q(G1),1)
        self.assertEqual(round(self.m.calculate_q(G1),2),0.2)
        G1.clear()

    def test_main(self):
        result=self.m.main()
        self.assertEqual(result,self.m.iterations)#to check if the  proposed graph is different from the previous graph
        self.m.G1.clear()
        self.m.G2.clear()


    def test_theta_func(self):

        G=nx.star_graph(4)
        self.assertNotEqual(self.m.theta_func(G),0)

''' def test_stationary(self):
        result=self.m.main
        self.assertGreater(self.m.test_stationary(),)'''
