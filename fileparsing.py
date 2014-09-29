# -*- coding: utf-8 -*-

import optparse
import fileinput
import sys

parser = optparse.OptionParser("usage%prog -c <countername> -d <directory>")
parser.add_option('-c', dest='counter', type='string',help='notify me about talking counter')
parser.add_option('-d', dest='directory', type='string', help='notify me about log path')
(options, args) = parser.parse_args()

cname = options.counter
dname = options.directory

def replaceKAKAO(file):
    for line in fileinput.input(file, inplace=1):
        if "년 " in line:
            line = line.replace("년 ", ",")
        if "월 " in line:
            line = line.replace("월 ", ",")
        if "일 " in line:
            line = line.replace("일 ", ",")
        if "오후 " in line:
            line = line.replace("오후 ", ",")
        if ":" in line:
            line = line.replace(":", ",")
        if " 회원님 " in line:
            line = line.replace(" 회원님 ", "me")
        if counter in line:
            line = line.replace(cname, "counter")

        sys.stdout.write(line)

def remove_12line(file):
    for line_number, line in enumerate(fileinput.input(file, inplace=1)):
        if line_number == 0:
            continue
        if line_number == 1:
            continue
        else:
            sys.stdout.write(line)

remove_12line(dname)
replaceKAKAO(dname)

