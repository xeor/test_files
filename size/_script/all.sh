#!/bin/bash

dd if=/dev/zero of=1MiB bs=1k count=1024
dd if=/dev/zero of=1MB bs=1000 count=1000

dd if=/dev/zero of=1KiB bs=1k count=1
dd if=/dev/zero of=1KB bs=1 count=1000
