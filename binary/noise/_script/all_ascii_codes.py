#!/usr/bin/env python

open('all_ascii_codes', 'w').write(''.join([ chr(i) for i in xrange(256) ]))
