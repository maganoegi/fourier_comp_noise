



import unittest
import random
from fourier import tfd, tfd2, tfdi, tfdi2

class TestValidator(unittest.TestCase):

	def setUp(self):
		# constants here
        # self.blabla
        pass


	def test_ttl_update(self):
		"""----- see whether the ttl value is degraded with time ------"""
		s = Signal(self.alert_template, self.regular_sensitive)
		s.TTL = 0 # putting it manually, as normally it is attributed in process() upon first contact
		ttl_update([s])
		self.assertEqual(s.TTL, -1)


		


def run_tests():
	print("Executing unit tests...\n")
	unittest.main(verbosity=2)  # executes unit tests on execution
                                # 0: quiet, 
                                # 1: dots or F, 
                                # 2: test functions names

   
if __name__ == '__main__':
	run_tests()
