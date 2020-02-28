#!/usr/bin/env python

__author__ = "Tiziano Mele"
__license__ = "MIT"
__version__ = "0.8"
__maintainer__ = "Tiziano Mele"
__email__ = "onaizitelem@gmail.com"
__status__ = "Development"

from loggen import Loggen
from conf_reader import ConfReader
import os

## Reading config from yaml
config = ConfReader(os.getcwd() + "/config.yaml")
thread_name = "Logger1"
filepath = config.get_outfile()
lines = config.get_template_lines()
no_bulk_lines = config.get_no_bulk_lines()
sleep_time = config.get_sleep_time()
no_total_lines = config.get_no_total_lines()
prefix_no_lines = config.get_prefix_no_lines()

## Preparing..
logger = Loggen(thread_name, filepath, lines, no_bulk_lines, sleep_time, no_total_lines, prefix_no_lines)
## ..and starting thread
logger.start()
print("Started Loggen thread..")

## Wait until thread exits
logger.join()
print("Finish")

## Bye bye