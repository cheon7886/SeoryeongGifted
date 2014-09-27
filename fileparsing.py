# -*- coding: utf-8 -*-

import fileinput
import sys

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
	if " 보기드문남자♥ " in line:
	    line = line.replace(" 보기드문남자♥ ", "counter")


	sys.stdout.write(line)

replaceKAKAO("Downloads/KakaoTalkChats.txt")
