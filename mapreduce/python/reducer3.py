#!/usr/bin/env python3

import sys

data = {}

for line in sys.stdin:
    try:
        line = line.strip()
        severity, path = line.split("\t", 1)

        path = float(path)

        severity_data = data.get(severity, list([0, 0]))
        severity_data[0] += path
        severity_data[1] += 1
        data[severity] = severity_data
    except Exception as e:
        continue

try:
    for k, v in data.items():
        print(f"Severity: {k}. Avg path len: {v[0] / v[1]}")
except Exception as e:
    pass

