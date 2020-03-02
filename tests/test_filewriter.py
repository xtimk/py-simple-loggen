import unittest
from file_writer import File_writer
import os

class basic_filewriter_unittest(unittest.TestCase):

	def get_file_no_lines(self, filepath):
		no_lines = 0
		with open(filepath, 'r') as f:
			for line in f:
				no_lines += 1

		return no_lines

	def test_constructor_file_creation(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		clear_existing_file_data = True
		## ---

		logger = File_writer(filepath, clear_existing_file_data, lines, prefix_no_lines)
		result = os.path.isfile(filepath)
		self.assertTrue(result)

	def test_constructor_clearing_existing_data(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		clear_existing_file_data = True
		## ---

		## Create file and write a test line
		filehandle = open(filepath,"w")
		filehandle.write("testing line\n")
		filehandle.close()

		## 
		logger = File_writer(filepath, clear_existing_file_data, lines, prefix_no_lines)
		## Expected behaviour: filepath exists AND filepath is empty (i.e. size is 0)
		result = os.path.isfile(filepath) and (os.stat(filepath).st_size == 0)
		self.assertTrue(result)

	def test_constructor_mantaining_existing_data(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		clear_existing_file_data = False
		## ---

		## Create file and write a test line
		filehandle = open(filepath,"w")
		filehandle.write("testing line\n")
		filehandle.close()

		## 
		logger = File_writer(filepath, clear_existing_file_data, lines, prefix_no_lines)
		## Expected behaviour: filepath exists AND filepath is not empty (i.e. size is not 0)
		result = os.path.isfile(filepath) and (os.stat(filepath).st_size > 0)
		self.assertTrue(result)

	def test_get_rand_line(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		clear_existing_file_data = True
		## ---

		logger = File_writer(filepath, clear_existing_file_data, lines, prefix_no_lines)
		result = (logger.get_rand_line() in lines)
		self.assertTrue(result)

	def test_bulk_append_number_of_lines(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		bulk_size = 10
		clear_existing_file_data = True
		## ---

		logger = File_writer(filepath, clear_existing_file_data, lines, prefix_no_lines)
		logger.append_bulk(bulk_size)

		result = self.get_file_no_lines(filepath)

		self.assertEqual(result, bulk_size)

	def test_single_append_number_of_lines(self):
		## input data
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		prefix_no_lines = True
		clear_existing_file_data = True
		## ---

		logger = File_writer(filepath, clear_existing_file_data, lines, prefix_no_lines)
		logger.append_single_line()

		result = self.get_file_no_lines(filepath)

		self.assertEqual(result, 1)

if __name__ == '__main__':
	unittest.main()
