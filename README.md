[![Build Status](https://travis-ci.com/xtimk/py-simple-loggen.svg?branch=master)](https://travis-ci.com/xtimk/py-simple-loggen)
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
template_lines: ["p1", "p2", "p3", "p4"]
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
