#!/usr/bin/env python

buf = ''
with open('100x100_x.txt', 'w') as fp:
    for a in xrange(100):
        for b in xrange(100):
            buf += 'x'
        buf += '\n'
    fp.write(buf.strip())