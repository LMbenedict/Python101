#! /usr/bin/env python

#this code will read and calculate things from DNA sequences (not really)


#define a variable and print the sequence
DNASeq = 'ATGAAC'
#DNASeq = input("Enter a DNA sequence: ")	#waits for input from command line to assign to DNASeq
DNASeq = DNASeq.upper()
print('Sequence:', DNASeq)

SeqLength = float(len(DNASeq))
print('Sequence Length:', SeqLength)

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT = DNASeq.count('T')

print("A:", NumberA/SeqLength)
print("C:", NumberC/SeqLength)
print("G:", NumberG/SeqLength)
print("T:", NumberT/SeqLength)

print("There are %d A bases." % (NumberA))

print("A occurs in %d bases out of %d." % (NumberA, SeqLength))
print("A occurs in %.2f of %d bases." % (100*NumberA/SeqLength, SeqLength))
