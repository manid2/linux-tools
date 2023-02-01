#!/usr/bin/python3

import re
from sys import argv
from pathlib import Path

# write the new tags to the following C syntax file
syntax_file = '/home/ubuntu/.vim/after/syntax/c/c-syn-pl2fw.vim'

# define basic regexes for the types to capture. These are quite crude for the
# structs and especially functions, but works for my functions/structs
with open(argv[-1), 'r') as f: input_data=f.read()
typedefs = re.findall(r'typedef\s+struct\s+([^\s{]+).+}\s*\1\s*;', input_data, re.DOTALL)
enums = re.findall(r'typedef\s+enum\s{[^}]+}\s+(\w+)\s*;', input_data, re.DOTALL)
functions = re.findall(r'(?:^|\n)(?:[\w*]+\s){1,2}(\w+)(?=\s*\()', input_data, re.DOTALL)

# See what we've already written
with open(syntax_file, 'r') as f: existing=f.read()

# If we haven't added it manually, append a line to the file with it
with open(syntax_file, 'a') as f:
    for tag in (typedefs + enums):
        format_string = 'syn keyword StorageClass %s\n' % tag
        if format_string not in existing: f.write(format_string)
    for tag in functions:
        if re.search(r'\nsyn keyword .+ %s\s' % tag, existing): continue
        f.write('syn keyword function %s\n' % tag)
