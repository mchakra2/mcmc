#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mcmc
----------------------------------

Tests for `mcmc` module.
"""

import math
import sys
import unittest
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

    

