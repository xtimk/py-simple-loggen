import unittest
from loggen import Loggen
import os

class basic_loggen_unittest(unittest.TestCase):

	def get_file_no_lines(self, filepath):
		no_lines = 0
		with open(filepath, 'r') as f:
			for line in f:
				no_lines += 1

		return no_lines

	def test_loggen_no_lines(self):
		## input data
		thread_name = "Logger1"
		filepath = os.getcwd() + "/tests/logtest.txt"
		lines = ["p1", "p2", "p3", "p4"]
		no_bulk_lines = 8
		sleep_time = 1
		no_total_lines = 22
		prefix_no_lines = True
		## ---

		logger = Loggen(thread_name, filepath, lines, no_bulk_lines, sleep_time, no_total_lines, prefix_no_lines)
		logger.start()
		logger.join()

		result = self.get_file_no_lines(filepath)
		self.assertEqual(result, no_total_lines)

if __name__ == '__main__':
	unittest.main()
