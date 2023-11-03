#!/usr/bin/env python3

import sys

current_severity = None
current_count = 0
severity = None

for line in sys.stdin:
    try:
        line = line.strip()
        severity, count = line.split("\t", 1)
        count = int(count)
        if current_severity == severity:
            current_count += count
        else:
            if current_severity:
                print("%s\t%s" % (current_severity, current_count))
            current_count = count
            current_severity = severity
    except Exception as e:
        continue

try:
    if current_severity == severity:
        print("%s\t%s" % (current_severity, current_count))
except Exception as e:
    pass

