import unittest
from file_writer import File_writer
import os

class basic_filewriter_unittest(unittest.TestCase):

	def test_constructor(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		## ---

		logger = File_writer(filepath, lines, prefix_no_lines)
		result = os.path.isfile(filepath)
		self.assertTrue(result)

	def test_get_rand_line(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		## ---

		logger = File_writer(filepath, lines, prefix_no_lines)
		result = (logger.get_rand_line() in lines)
		self.assertTrue(result)

	def test_bulk_append_number_of_lines(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		bulk_size = 10
		## ---

		logger = File_writer(filepath, lines, prefix_no_lines)
		logger.append_bulk(bulk_size)

		result = 0
		with open(filepath, 'r') as f:
			for line in f:
				result += 1

		self.assertEqual(result, bulk_size)

	def test_single_append_number_of_lines(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		## ---

		logger = File_writer(filepath, lines, prefix_no_lines)
		logger.append_single_line()

		result = 0
		with open(filepath, 'r') as f:
			for line in f:
				result += 1

		self.assertEqual(result, 1)

if __name__ == '__main__':
	unittest.main()
