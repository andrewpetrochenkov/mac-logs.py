#!/usr/bin/env python
import mac_logs

filenames = ["err.log", "error.log", "stderr.log"]

logs = mac_logs.logs(filenames=filenames)
print("filenames = %s (%s):\n%s" % (filenames, len(logs), "\n".join(logs)))
