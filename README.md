#XeonPulse

Project for Mathematical Psychologic Analysis By Using Messenger Logs

**optparse was deprecated from python, and argparse is newer version. So this code cannot be used by current version of python. We'll work with this problem as soon as possible.**

This repository contains some python script for data analyzing.

We're working for making a mind analyzing framework, and for long-term evolution, we're uploading all files.

Thank you.

##Usage

We categrized processes of data analysis by three codes, to have a compatibility with parallel processing. 

In the case of large files, we recommend PyPy.    
You can install it like this(if you use Ubuntu):

    'sudo apt-get install pypy'

Build source can be found from here: [raw binary](http://pypy.org/download.html).

##Run

This code is for linux users, So i used option parsing for convenience.

Fileparsing.py: make raw a KakaoTalk log into parsable-formed csv file.    
It delete korean strings and replace senders' name.

    sudo python fileparsing.py -c <countername> -d <directory> -o <outputfile>
    
CSVRefiner.py: refine csv file's times into minute-series.

    sudo python CSVRefiner.py -f <filedirectory> -o <outputdir>

FinalSorter.py: select useful keyword of specific sender, and run cumulative summing.

    sudo python FinalSorter.py -w <whoname> -k <keyword> -d <directory>
