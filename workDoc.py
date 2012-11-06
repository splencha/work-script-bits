#!/usr/bin/env python

import os
import sys

choice = raw_input('What doc needs to be filled out? (choose time, travel, daily, or monthly)')
def file_open():
    if choice.lower() == 'time':
        os.system('/usr/bin/gnome-open /home/david/Documents/LI/Timesheets/TimeSheet_Mon-xx-year.xls')
    if choice.lower() == 'travel':
        os.system('/usr/bin/gnome-open /home/david/Documents/LI/Travel/"Travel form_Mon-xx-year.xls"')
    else:
        print "That choice is not yet supported."
        sys.exit()

file_open()
