#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")
    try:
        print("%s\t%s" % (data[2], data[9]))
    except Exception as e:
        continue
