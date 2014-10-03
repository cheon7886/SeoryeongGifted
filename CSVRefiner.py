import pandas as pd
import optparse
import sys

parser = optparse.OptionParser("usage%prog -f <filedirectory> -o <outputdir>")
parser.add_option('-f', dest='filedirectory', type='string', help='specify filedirectory')
parser.add_option('-o', dest='outputdir', type='string', help='specify outputdir')
(options, args) = parser.parse_args()

file_dir = options.filedirectory
output_dir = options.outputdir
result = pd.read_csv(file_dir, names=['year','month','day','am/pm','time','minute','sender','data'], sep='|')

# define initial values

firstyear=result.iloc[0,0] 
series1 = result['year']
series2 = result['month']
series3 = result['day']
series4 = result['am/pm']
series5 = result['time']
series6 = result['minute']
series7 = result['sender']
series8 = result['data']

# make minute merge

series1 = (series1 - firstyear) * 518400
series2 = series2 * 43200
series3 = series3 * 1440
series5 = series5 * 60

#start Final Frame

Mid_series = series1 + series2 + series3 + series4 + series5 + series6
FirstTime = Mid_series.iloc[0]
Mid_series = Mid_series - FirstTime
Fin_frame = pd.concat([Mid_series, series7, series8], axis=1, keys=['Time','Sender','Data'])
Fin_frame = Fin_frame.set_index('Time')
Fin_frame.to_csv(output_dir, sep='|')
