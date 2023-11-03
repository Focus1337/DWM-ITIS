#!/usr/bin/env python3

import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    price = fields[1].strip('"')
    postcode = fields[3]

    print(f"{postcode}\t{price}")