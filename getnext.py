#!/usr/bin/python3.8

# 'pip install gspread' -- google sheets API
import gspread, os
dsh = "-" * 60

# get the current directory of the script...
curdir = os.path.dirname(os.path.abspath(__file__))


gc = gspread.service_account(filename = curdir + '/getnextcreds.json') 
wsh = gc.open('Budg').worksheet('Last')

val = wsh.get_values('alltasks')

for i in range(len(val)):
    if i == 0:
        print(dsh)
        print('{:<25}{:<15}{:<15}{:<15}'.format(val[i][0],val[i][1],val[i][2],val[i][3]))
        print(dsh)
    else:
        print('{:<25}{:<15}{:<15}{:<15}'.format(val[i][0],val[i][1],val[i][2],val[i][3]))


