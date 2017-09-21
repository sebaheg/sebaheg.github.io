#!/usr/bin/env python

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    print(filename)
    f = open(filename, 'r', encoding="utf8")
    crawl = False
    live = False
    current_tags = []
    for line in f:
        if crawl:
            current_line = line.strip().split()
            print(current_line)
            if current_line[0] == 'live:':
                if current_line[1] == 'true':
                    live = True
            if current_line[0] == 'tags:':
                current_tags = current_line[1:]
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    if live == True:
        total_tags.extend(current_tags)


    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
