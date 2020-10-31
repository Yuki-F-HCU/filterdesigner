import unittest
import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
import filterdesigner.FIRDesign as FIRDesign

class TestFIRpm(unittest.TestCase):
    def setUp(self):
        self.n1 = 17
        self.f1 = np.array([0, 0.3, 0.4, 0.6, 0.7, 1])
        self.a1 = [0, 0, 1, 1, 0, 0]

        self.n2 = 50
        self.fs = 1000
        self.f2 = np.array([0, 150, 200, 300, 350, 500])
        self.a2 = [0, 0, 1, 1, 0, 0]
        self.w = [3, 1, 100]

    def test_firpm_1(self):
        x = [i for i in range(len(self.f1))]
        ipf = ip.interp1d(x, self.f1)
        f1_new = ipf(np.linspace(x[0], x[-1], 2*len(x)))

        self.assertTrue(FIRDesign.firpm(self.n1, self.f1, self.a1) == (signal.remez(self.n1+1, f1_new, self.a1), 1))

    def test_firpm_2(self):
        x = [i for i in range(len(self.f2))]
        ipf = ip.interp1d(x, self.f2)
        f2_new = ipf(np.linspace(x[0], x[-1], 2*len(x)))

        self.assertTrue(FIRDesign.firpm(self.n2, self.f2, self.a2, self.w) == (signal.remez(self.n2+1, f2_new, self.a2, self.w), 1))