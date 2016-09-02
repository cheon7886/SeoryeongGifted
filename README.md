#XeonPulse

Project for Mathematical Psychologic Analysis By Using Messenger Logs

**optparse was deprecated from python, and argparse is newer version. So this code cannot be used by current version of python. We'll work with this problem as soon as possible.**

This repository contains some python script for data analyzing.

We're working for making a mind analyzing framework, and for long-term evolution, we're uploading all files.

Thank you.

##Model

<img src="https://github.com/cheon7886/XeonPulse/blob/master/img/Topology.png" width="400px">

We defined psychological model like above: this consists of **layers :** <img src="https://github.com/cheon7886/XeonPulse/blob/master/img/Entry.png" width="180px">,    
which are constructed by **elements :** <img src="https://github.com/cheon7886/XeonPulse/blob/master/img/Layer.png" width="180px">    
and **'elements'** group contains coordinates made from three codes below.
<img src="https://github.com/cheon7886/XeonPulse/blob/master/img/Element.png" width="265px">    
every element have relationship with each other, and that 'relationship' is named **affection rate**(residual value).
<img src="https://github.com/cheon7886/XeonPulse/blob/master/img/AffRate.png" width="140px">

|Stage of Process| Keyword: "이모티콘"(3122 found)| Keyword: "ㅎ"(642 found)|
| :-------------: | :-------------: |:-------------:|
|**Refined Data**| <img src="https://github.com/cheon7886/XeonPulse/blob/readme/img/emo3.png"> | <img src="https://github.com/cheon7886/XeonPulse/blob/readme/img/h03.png"> |
|**After Regression**| <img src="https://github.com/cheon7886/XeonPulse/blob/readme/img/emo1.png"> | <img src="https://github.com/cheon7886/XeonPulse/blob/readme/img/h01.png"> |
|**The Derivative**| <img src="https://github.com/cheon7886/XeonPulse/blob/readme/img/emo2.png"> | <img src="https://github.com/cheon7886/XeonPulse/blob/readme/img/h02.png"> |

##Algorithm

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
