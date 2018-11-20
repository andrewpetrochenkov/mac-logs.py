[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-logs.svg?longCache=True)](https://pypi.org/pypi/mac-logs/)
[![](https://img.shields.io/pypi/v/mac-logs.svg?maxAge=3600)](https://pypi.org/pypi/mac-logs/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-logs.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-logs.py/)

#### Install
```bash
$ [sudo] pip install mac-logs
```

#### Features
`~/Library/Logs` MacOS `.log` files

#### Functions
function|description
-|-
`mac_logs.errors()`|return list of `*err*.log` files (`stderr.log`, `err.log`, `error.log`, ...)
`mac_logs.logs(filenames=None, minsize=0)`|return list of `.log` files
`mac_logs.reveal()`|reveal `~/Library/Logs` in Finder
`mac_logs.rm(filenames=None, minsize=0)`|remove `.log` files
`mac_logs.tag()`|set Finder tag. `red` - not empty error logs, `none` - other logs

#### CLI
usage|description
-|-
`python -m mac_logs.tag`|set Finder tag. `red` - not empty error logs, `none` - other logs

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>