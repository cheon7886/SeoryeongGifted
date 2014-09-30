# -*- coding: utf-8 -*-

import optparse
import fileinput
import sys
import csv

parser = optparse.OptionParser("usage%prog -c <countername> -d <directory> -o <outputfile>")
parser.add_option('-c', dest='counter', type='string',help='notify me about talking counter')
parser.add_option('-d', dest='directory', type='string', help='notify me about log path')
parser.add_option('-o', dest='outputfile', type='string', help='specify about outputcsv file name')

(options, args) = parser.parse_args()

cname = options.counter
dname = options.directory
fname = options.outputfile

def convertcsv(in_file,out_file):
    fin_txt = csv.reader(open(in_file, "rb"), delimiter = ',')
    out_csv = csv.writer(open(out_file, 'wb'))
    out_csv.writerows(fin_txt)

def replaceKAKAO(file):
    for line in fileinput.input(file, inplace=1):
        if "년 " in line:
            line = line.replace("년 ", ",")
        if "월 " in line:
            line = line.replace("월 ", ",")
        if "일 " in line:
            line = line.replace("일 ", ",")
        if "오전 " in line:
            line = line.replace("오전 ", "morning,")
        if "오후 " in line:
            line = line.replace("오후 ", "afternoon,")
        if ":" in line:
            line = line.replace(":", ",")
        if " 회원님 " in line:
            line = line.replace(" 회원님 ", "me")
        if cname in line:
            line = line.replace(cname, "counter")
        if ", " in line:
            line = line.replace(", ", ",")
        else:
            print "Countername was not found"
            exit(0)
            sys.stdout.write(line)

def remove_12line(file):
    for line_number, line in enumerate(fileinput.input(file, inplace=1)):
        if line_number == 0:
            continue
        if line_number == 1:
            continue
        if line_number == 2:
            continue
        if line_number == 3:
            continue
        else:
            sys.stdout.write(line)

if (cname == None) | (dname == None) | (fname == None):
    print parser.usage
    exit(0)
else :
    remove_12line(dname)
    replaceKAKAO(dname)
    convertcsv(dname,fname)
