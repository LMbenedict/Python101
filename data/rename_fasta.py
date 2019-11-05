#! /usr/bin/env python

#GOAL: replace name row with "Homo_sapiens" followed by numeric string at beginning, in fasta format (no spaces, > at beginning)

#Pseudocode: 
"""
import reg ex package

open.file = "fast file name"
open.fasta.file = (open.file, 'r')
open.out.file.name = "outfile name.fasta"
open.out.file = (out.file.name, 'w')


for Line in fasta.file:
	Line = Line.strip('\n')
	if Line begins with >
		Find = regex for the name line of the file
		Result = re.search(find, Line)
		out.file.write(">Homo_sapiens: Result\n")
	else: 
		out.file.write("Line\n")


fasta.file.close = ()
out.file.close = ()


"""

#Real code:

#ATTN Julie: I this script correctly uses regex and prints what I would like to the screen
#However, it does not print to the outfile. I am having trouble figuring out why.

import re

InFileName = "regex.practice1.fasta"
InFile = open(InFileName, 'r')
OutFileName = "regex.practice1.ed.txt"
OutFile = open(OutFileName, 'w')


for Line in InFile:
	Line = Line.strip('\n')
	if Line.startswith('>'):
		Find = r"^>(\d{4}_\d:\w{6})\s\{.*?\}"
		Result = re.search(Find, Line)
		Name = Result.group(1)
		OutFile.write(">Homo_sapiens: %s\n" % (Name))
		print(">Homo_sapiens: %s" % (Name))
	else: 
		OutFile.write("%s\n" % (Line))
		print("%s" % (Line))
	


InFile.close = ()
OutFile.close = ()