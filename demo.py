#!/usr/bin/env python3

import time

runtime_seconds = 300
result_count = 1500
result_lines = 10

sleep_seconds = runtime_seconds / result_count

for result in range(1, result_count + 1):
    print('Result {result}'.format(result=result))

    for line in range(1, result_lines - 1):
        print('  Line {line}'.format(line=line))

    print()

    time.sleep(sleep_seconds)
