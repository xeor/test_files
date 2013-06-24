#!/usr/bin/env python

open('utf-8_0-ffff', 'w').write(''.join([ unichr(i) for i in xrange(65535) ]).encode('utf-8'));
