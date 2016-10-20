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

    def test_dist_arg_type(self):
       
        with self.assertRaises(TypeError):
            self.m.dist((-4,1),1)
        with self.assertRaises(TypeError):
            self.m.dist(2.2,'a')
        with self.assertRaises(TypeError):
            self.m.dist(('A',3),(2.2,1))
        #self.assertRaises(TypeError,self.m.dist,[2,3])
        #self.assertRaises(TypeError,self.m.dist,[2.3,3.2])

        #self.assertRaises(TypeError,self.m.dist,['a','b'])
        #self.assertRaises(TypeError,self.m.dist,[(2,3),(3.2)])
    def test_dist_return(self):
        
        val=round(math.sqrt(2.2**2+2.2**2),2)
        wt=self.m.dist((2.2,2.2), (0,0))
        self.assertEqual(round(wt,2),val)

    
    def test_input_file(self):
           
        self.assertRaises(IOError,self.m.input_arg,'random_file_which_should_not_exist.txt')
        #self.m.main()
        flag = os.path.getsize(self.m.input_f)
        self.assertGreater(flag,0)

    def test_tuples(self):
        self.m.input_arg(self.m.input_f)
        self.assertGreater(len(self.m.M),0)#To ensure that the number of vertices is greater than 0

    def test_make_init_graph(self):
        self.m.input_arg(self.m.input_f)
        self.m.make_init_graph()
        self.assertIsInstance(self.m.G,nx.Graph)
        self.assertTrue(nx.is_connected(self.m.G),'Initial Graph is not connected')
        
