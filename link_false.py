#!/usr/bin/env python

import glob, os
import fileinput

os.chdir('./_includes/_plots')
for file in glob.glob('*.html'):
    with fileinput.FileInput(file, inplace=True) as content:
        for line in content:
            print(line.replace('true', 'false'), end='')
