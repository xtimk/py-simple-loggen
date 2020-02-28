#!/usr/bin/env python

__author__ = "Tiziano Mele"
__license__ = "MIT"
__version__ = "0.8"
__maintainer__ = "Tiziano Mele"
__email__ = "onaizitelem@gmail.com"
__status__ = "Development"

from threading import Thread
from file_writer import File_writer
import time

class Loggen(Thread):
	filepath = ""
	source_lines = []

	def __init__(self, thread_name, filepath, source_lines, no_bulk_lines, sleep_time, no_total_lines, prefix_no_lines):
		Thread.__init__(self)
		self.name = thread_name
		self.filepath = filepath
		self.source_lines = source_lines
		self.no_bulk_lines = no_bulk_lines
		self.sleep_time = sleep_time
		self.no_total_lines = no_total_lines
		self.prefix_no_lines = prefix_no_lines

		self.fw = File_writer(self.filepath, self.source_lines, self.prefix_no_lines)


	def run(self):
		# print("Thread <" + self.name + "> started.")
		total_written_lines = 0
		while total_written_lines < self.no_total_lines:
			if (self.no_total_lines - total_written_lines >= self.no_bulk_lines):
				self.fw.append_bulk(self.no_bulk_lines)
				total_written_lines += self.no_bulk_lines
				time.sleep(self.sleep_time)
			else:
				self.fw.append_bulk(self.no_total_lines - total_written_lines)
				total_written_lines += self.no_total_lines - total_written_lines
				time.sleep(self.sleep_time)
		# print("Thread <" + self.name + "> ended.")
		# print("Total written lines: " + str(total_written_lines))
		# print("Expected written lines: " + str(self.no_total_lines))

