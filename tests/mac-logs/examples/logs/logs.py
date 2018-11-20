#!/usr/bin/env python
import mac_logs

logs = mac_logs.logs()
print("all logs (%s):\n%s" % (len(logs), "\n".join(logs)))
