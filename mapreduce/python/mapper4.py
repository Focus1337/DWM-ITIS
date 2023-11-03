#!/usr/bin/env python3

import sys

for line in sys.stdin:
    fields = line.strip().split(',')

    transaction_id = fields[0]
    price = fields[1]
    date = fields[2]
    postcode = fields[3]

    print(f"{transaction_id}\t{price}\t{date}\t{postcode}")