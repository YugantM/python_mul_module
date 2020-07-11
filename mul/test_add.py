import unittest
import mul

class TestClass(unittest.TestCase):
	def test_function(self):
		result = mul.mul(2,4)
		self.assertEqual(result,8)

if __name__ == "__main__":
	unittest.main()
