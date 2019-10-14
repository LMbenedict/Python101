#! /usr/bin/env python

#Aim: convert sentence from command line into lower case, remove spaces, count length
#Student: Lauren Benedict, BIOL792, Fall 2019


#Pseudocode:
#create variable from input
#turn to lowercase
#remove spaces (and punctuation) from sentence variable
#count the length
#print the length


#prompt input
sentence = input("Enter sentence: ")

#turn to lowercase
sentenceL = sentence.lower()

#remove spaces, commas, and periods and assign to new variable
new_sentence = sentenceL.replace(" ","") 
new_sentence = new_sentence.replace(",","")
new_sentence = new_sentence.replace(".","")

#check that new_sentence is accurate
print(new_sentence)

#count length
print("Length: ", len(new_sentence))