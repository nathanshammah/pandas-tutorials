#!/usr/bin/env python
import sys


result = []
for line in sys.stdin:
    values = line.split(',', maxsplit=int(sys.argv[1]) - 1)
    values[-1] = '"{}"\n'.format(values[-1].rstrip('\n')
                                           .replace('"', '""'))
    sys.stdout.write(','.join(values))
