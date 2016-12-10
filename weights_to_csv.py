#!/usr/bin/env python3

import tkinter as tk
import tkinter.filedialog as tkF
import itertools
import sys

root = tk.Tk()
root.withdraw()
root.update()
read_file = tkF.askopenfilename()

write_file = input("Enter output filename:")

if write_file[-4:] != ".csv":
	write_file = write_file + ".csv"

print("Now converting " +read_file)

try: 
	with open(read_file, 'r') as rf: 
		with open(write_file, 'w') as wf:
			# Skip first two lines: start=3, stop=None
			for line in itertools.islice(rf, 3, None):  
				split_line = line.split()
				wf.write(split_line[1] + ",")
				wf.write(split_line[2] + ",")
		
		print("All done! Output located at " + write_file + "\n")


except IndexError:
	print("Some line had fewer than 3 columns. Unable to continue")
except:
	print("Unable to process this file. :(")

input("Press any key to exit")


	

