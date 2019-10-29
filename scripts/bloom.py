#! /usr/bin/env python

#Goal: print taxon name and daidromous status, print out total log body size for all individuals


#Pseudocode

#InBloomFile = "file name"
#InBloom = open()

#LineNumber = 0
#TotalLogBody=0

#for Line in InBloom:
#  if the line is not zero:
#    strip line of line ending
#    split by commas
#    print first and last columns (column 0 and 3)
#    add 2nd column (column 1) to TotalLogBody
#  add 1 to LineNumber

#  close InBloom


#Real code

#read in and open file
InBloomFile = "Bloom_etal_2018_Reduced_Dataset.csv"
InBloom = open(InBloomFile, 'r')

#create line number to omit header
LineNumber = 0
#create variable for total log body 
TotalLogBody = 0

#create variables for diadromous counts
DiadCount = 0
NonDiadCount = 0

#for loop through each line of Bloom dataset
for Line in InBloom:
  #omit the header
  if LineNumber > 0:
    #remove line ending
    Line = Line.strip('\n')
    #split csv file to an array
    Elements = Line.split(',')
    #print the name and the status
    print("%s\t%s" % (Elements[0], Elements[3]))
    #convert string from column for log body weight to decimal
    LogBody = float(Elements[1])
    #add each line's log body weight to the total variable
    TotalLogBody = TotalLogBody + LogBody

    if Elements[3] == "diadromous":
      DiadCount = DiadCount + 1
    else:
      NonDiadCount = NonDiadCount + 1
  #increase line number count by 1
  LineNumber = LineNumber + 1


#print total log body size for all indivdiuals to screen
print("Total Log Body Size: ", TotalLogBody)
print("Total Diadramous: ", DiadCount)
print("Total Non-Diadramous: ", NonDiadCount)


#close file
InBloom.close()