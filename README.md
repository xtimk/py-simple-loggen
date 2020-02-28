[![Build Status](https://travis-ci.com/xtimk/py-simple-loggen.svg?branch=master)](https://travis-ci.com/xtimk/py-simple-loggen) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]([https://github.com/xtimk/py-simple-loggen/blob/master/LICENSE](https://github.com/xtimk/py-simple-loggen/blob/master/LICENSE)) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python 3.7.1](https://img.shields.io/badge/python-3.7.1-blue.svg)](https://www.python.org/downloads/release/python-371/)

# Simple Log Generator Utility

Simple log generator utilty written in python.

## Configuration
You can edit the `config.yaml` file to match your needs

Specify the output log file
```
outfile: 'tests/outfile.txt'
```
Specify a list of possibile lines that will be chosen casually and written in the log file
```
template_lines: ["example line 1", "example line 2", "example line 3"]
```
How many lines do you want to write at one time. If you want to increase write speed increase this number
```
no_bulk_lines: 10
```
How many second to wait between writes. For example you can increase this if you want to decrease write speed
```
sleep_time: 1
```
How many lines will be written in total in the log file
```
no_total_lines: 15
```
Flag that if enabled prepends the line number in each log line
```
prefix_no_lines: True
```
## Starting
You can start generating your log by launching loggen.py
```
python3 loggen.py
```

That's it!
