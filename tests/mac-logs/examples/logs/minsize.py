#!/usr/bin/env python
import mac_logs

minsize = 1

logs = mac_logs.logs(minsize=minsize)
print("not empty logs (%s):\n%s" % (len(logs), "\n".join(logs)))
