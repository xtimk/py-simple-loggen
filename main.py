from loggen import Loggen

thread_name = "Logger1"
filepath = "/Users/tiz/Desktop/py-simple-loggen/test.txt"
lines = ["p1\n", "p2\n", "p3\n", "p4\n"]
no_bulk_lines = 10
sleep_time = 1
no_total_lines = 58
prefix_no_lines = True

logger = Loggen(thread_name, filepath, lines, no_bulk_lines, sleep_time, no_total_lines)
logger.start()
logger.join()

print("End of main")