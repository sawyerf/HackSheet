#!/bin/bash

import os
import re

def format_link(file, title):
    fmt = re.findall(r'^(#*)# (.*)\n', title)[0]
    # print(fmt[0], fmt[1])
    index = fmt[0].replace('#', '  ')
    link  = fmt[1].lower()
    link  = re.sub(r'[()& ]', '-', link)
    return '{}- [{}](/wiki/{}#{})\n'.format(index, fmt[1], file, link)

wr = open('wiki/Index.md', 'w')
wr.write('# Index\n\n')
for file in sorted(os.listdir('wiki/')):
    if file == 'Index.md':
        continue
    print(file)
    with open('wiki/' + file, 'r') as fd:
        wr.write(format_link(file, fd.readline()))
        for line in fd.readlines():
            if re.match(r'^##', line):
                wr.write(format_link(file, line))