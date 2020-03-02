[![Build Status](https://travis-ci.com/xtimk/py-simple-loggen.svg?branch=master)](https://travis-ci.com/xtimk/py-simple-loggen) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]([https://github.com/xtimk/py-simple-loggen/blob/master/LICENSE](https://github.com/xtimk/py-simple-loggen/blob/master/LICENSE)) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python 3.7.1](https://img.shields.io/badge/python-3.7.1-blue.svg)](https://www.python.org/downloads/release/python-371/)

  

# Simple Log Generator Utility
Simple log generator utility written in python for my convenience. 

Basically this tool chooses casually from a set of user-defined logs and writes them into a file. 

You can find detailed infos in the `Configuration` section.

## Getting started
You'll need `python3` in order to run this project.

Clone/Download repo and enter in the root dir
```bash
git clone https://github.com/xtimk/py-simple-loggen.git
cd py-simple-loggen
```
Install prerequisites by running
```bash
pip3 install -r requirements.txt
```
Edit the `config.yaml` file to match your needs
```bash
nano config.yaml
```
Then simply run `loggen.py`
```bash
python3 loggen.py
```
## Configuration

Here is explained how to edit the `config.yaml`

Specifying the output log file

```yaml
outfile: 'tests/outfile.txt'
```

Specifying a list of possibile lines that will be chosen casually and written in the log file
```yaml
template_lines: ["example line 1",
"Mar  2 09:19:59 centos7-64 sshd[11942]: Accepted password for root from 192.168.100.151 port 49450 ssh2",
"Mar  2 09:19:41 centos7-64 login: ROOT LOGIN ON tty1"]
```

How many lines do you want to write at one time. If you want to increase write speed increase this number
```yaml
no_bulk_lines: 10
```

How many second to wait between writes. You can use also float values here. For example you can increase this if you want to decrease write speed
```yaml
sleep_time: 1
```

How many lines will be written in total in the log file
```yaml
no_total_lines: 15
```

Flag that if enabled prepends the line number in each log line

```yaml
prefix_no_lines: True
```

That's it folks!
