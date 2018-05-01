#!/usr/bin/env python3

import time


iterable = ['kenso', 'isroel', 'vince']

counter = 0
for iterator in iterable:
    counter += 1
    print('Count:', str(counter))
    print('This is an iteration \n')
    time.sleep(1)
