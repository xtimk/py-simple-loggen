from file_writer import File_writer

filepath = "/Users/tiz/Desktop/py-simple-loggen/test.txt"

lines = ["p1\n", "p2\n", "p3\n", "p4\n"]

logger = File_writer(filepath, lines)

# logger.append_single_line()
logger.append_bulk(10)