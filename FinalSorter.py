# -*- coding: utf-8 -*-

import pandas as pd
import fileinput
import optparse
import sys

parser = optparse.OptionParser("usage%prog -w <whoname> -k <keyword> -d <directory>")
parser.add_option('-w', dest='whoname', type='string', help='notify me about whom you want to choice')
parser.add_option('-k', dest='keyword', type='string', help='notify me about your keyword which you want to analyze')
parser.add_option('-d', dest='directory', type='string', help='notify me about log path')
parser.add_option('-o', dest='outputfile', type='string', help='notify me about where you want to save')

(options, args) = parser.parse_args()

wname = options.whoname
kname = options.keyword
dname = options.directory
oname = options.outputfile
result = pd.read_csv("Midfile.csv", sep='|')

result = result[result.Sender == wname]
del result['Sender']
result = result.dropna()
result = result[result['Data'].str.contains(kname)]
result['Data'] = 1
firsttime = result.iloc[0,0]
result['Time'] = result['Time'] - firsttime
result['Data'] = result['Data'].cumsum()
result = result.set_index('Time')
print result
print "Saved"
result.to_csv(oname, sep=',')