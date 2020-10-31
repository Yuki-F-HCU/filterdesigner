import unittest
import filterdesigner.FIRDesign as FIRDesign
import numpy as np
import scipy.signal as signal

class TestFIRls(unittest.TestCase):
    def setUp(self):
        self.n = 100
        self.f = [0, 0.15, 0.85, 1]
        self.a = [1, 1, 0, 0]
        
        self.n2 = 101

    def test_firls_1(self):
        # Test for least square method
        self.assertTrue(FIRDesign.firls(self.n, self.f, self.a) == (signal.firls(101, f, a), 1))
        
    def test_firls_2(self):
        # Test for least square method with odd order
        self.assertTrue(FIRDesign.firls(self.n2, self.f, self.a) == (signal.firls(103, f, a), 1))