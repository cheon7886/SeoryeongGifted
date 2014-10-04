#SeoryeongGifted
===============

Academia for Gifted Student in Seoryeong High School Github repository
This repository contains some python script for data analyzing.
We're working for making a mind analyzing framework, and for long-term evolution, we're uploading all files.
After finish main contest, we'll fill good document for everyone.
Thank you.

##Usage
This code need some time if you have large file, so i recommend PyPy.
You can install it like this(if you use Ubuntu):
'sudo apt-get install pypy'
If not, you need to build fully with [raw binary](http://pypy.org/download.html).

##Run
This code is for linux users, So i used option parsing for convenience.

Fileparsing.py: this is for making raw KakaoTalk file into data minable csv file.
It delete korean strings and replace senders' name.
'sudo python fileparsing.py -c <countername> -d <directory> -o <outputfile>'
CSVRefiner.py: this is for making csv file's times into minute-series.
'sudo python CSVRefiner.py -f <filedirectory> -o <outputdir>'
FinalSorter.py: this is for selecting useful keyword, one sender, and try cumulative summing.
'sudo python FinalSorter.py -w <whoname> -k <keyword> -d <directory>'
