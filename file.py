#!/usr/bin/env python
# coding: utf-8

import os
from re import sub
os.getcwd 



phone_list = []
with open('input_file.txt') as fo:
    for i in fo:
        phone_list.append(i.strip())


start_string = 'context atr-operators {\n'
end_string = '};'


with open('output_file.txt', 'w') as fo:
    fo.write(start_string)
    for number in phone_list:
        fo.write('\t_%s => {\n\t\tNoOp(Permission denied);\n\t\tHangup();\n\t};\n' % number)
    fo.write(end_string)


start_string = 'context atr-operators {\n'
end_string = '};'





