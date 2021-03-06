import unittest
import filterdesigner.IIRDesign as IIRDesign
import scipy.signal as signal
import numpy as np

class TestIirpeak(unittest.TestCase):

    def setUp(self):
        self.w0 = 0.4
        self.bw = 0.4/35

    def test_iirpeak_1(self):
        # Test case
        IIR = IIRDesign.iirpeak(self.w0, self.bw)
        iir = signal.iirpeak(self.w0, self.w0/self.bw, fs=2)
        self.assertTrue(np.all(IIR[0] == iir[0]) and np.all(IIR[1] == iir[1]))

    def test_iirpeak_2(self):
        # Test case for Exception 1
        with self.assertRaises(ValueError):
            IIRDesign.iirpeak(4, self.bw)

    def test_iirpeak_3(self):
        # Test case for Exception 2
        with self.assertRaises(ValueError):
            IIRDesign.iirpeak(self.w0, 40)
