#!/usr/bin/env python

__author__ = "Tiziano Mele"
__license__ = "MIT"
__version__ = "0.8"
__maintainer__ = "Tiziano Mele"
__email__ = "onaizitelem@gmail.com"
__status__ = "Development"

import random

class File_writer:
	filepath = ""
	source_lines = []

	def __init__(self, filepath, source_lines, prefix_no_line):
		self.filepath = filepath
		self.source_lines = source_lines
		self.prefix_no_line = prefix_no_line

		self.total_written_lines = 0
		filehandle = open(self.filepath,"w")
		filehandle.close()

	def get_rand_line(self):
		rand_index = random.randrange(len(self.source_lines))
		return self.source_lines[rand_index]

	def append_bulk(self, number_of_lines):
		try:
			filehandle = open(self.filepath,"a+")
			for i in range(number_of_lines):
				line = self.get_rand_line()
				if self.prefix_no_line:
					filehandle.write(str(self.total_written_lines + 1) + " " + line + "\n")
				else:
					filehandle.write(line + "\n")

				self.total_written_lines += 1

			filehandle.close()
		except Exception as e:
			print(e)
			exit(99)


	def append_single_line(self):
		try:
			line = self.get_rand_line()
			filehandle = open(self.filepath,"a+")
			if self.prefix_no_line:
				filehandle.write(str(self.total_written_lines + 1) + " " + line + "\n")
			else:
				filehandle.write(line + "\n")
			
			filehandle.close()
			self.total_written_lines += 1
		except Exception as e:
			print(e)
			exit(99)



