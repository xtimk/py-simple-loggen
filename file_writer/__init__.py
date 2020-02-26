import random

class File_writer:
	filepath = ""
	source_lines = []

	def __init__(self, filepath, source_lines):
		self.filepath = filepath
		self.source_lines = source_lines

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
				filehandle.write(line)
			filehandle.close()
		except Exception as e:
			print(e)
			exit(99)


	def append_single_line(self):
		try:
			line = self.get_rand_line()
			filehandle = open(self.filepath,"a+")
			filehandle.write(line)
			filehandle.close()
		except Exception as e:
			print(e)
			exit(99)



