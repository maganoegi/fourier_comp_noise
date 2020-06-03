


import numpy as np
import unittest
import random
from fourier import tfd, tfd2, tfdi, tfdi2

class TestValidator(unittest.TestCase):

    def setUp(self):
        # constants here
        # self.blabla
        self.bla = "bla"


    def test_tfd(self):
        x = np.random.random(1024)
        expected = np.fft.fft(x)
        obtained = tfd(x)

        self.assertTrue(np.allclose(expected, obtained))

    def test_tfdi(self):
        x = np.random.random(1024)
        f = tfd(x)
        expected = np.fft.ifft(f)
        obtained = tfdi(f)

        self.assertTrue(np.allclose(expected, obtained))

    def test_tfd2(self):
        dim = 12
        x = np.random.random((dim,dim))
        expected = np.fft.fft2(x)
        obtained = tfd2(x)

        self.assertTrue(np.allclose(expected, obtained))

    def test_tfdi2(self):
        dim = 12
        x = np.random.random((dim,dim))
        f = np.fft.fft2(x)

        expected = np.fft.ifft2(f)
        obtained = tfdi2(f)

        self.assertTrue(np.allclose(expected, obtained))

		


def run_tests():
	print("Executing unit tests...\n")
	unittest.main(verbosity=2)  # executes unit tests on execution
                                # 0: quiet, 
                                # 1: dots or F, 
                                # 2: test functions names

   
if __name__ == '__main__':
	run_tests()
