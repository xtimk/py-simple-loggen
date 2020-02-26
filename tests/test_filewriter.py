import unittest
from file_writer import File_writer
import os

class basic_filewriter_unittest(unittest.TestCase):

	def test_get_rand_line(self):
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1\n", "p2\n", "p3\n", "p4\n"]

		logger = File_writer(filepath, lines)
		result = (logger.get_rand_line() in lines)
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()
