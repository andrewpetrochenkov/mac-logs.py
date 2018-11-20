#!/usr/bin/env python
import mac_logs

print("%s .log files" % len(mac_logs.logs()))
mac_logs.rm()
print("%s .log files" % len(mac_logs.logs()))
