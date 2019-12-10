#! /usr/bin/env python

#Parse data from SagehenBandingFile to create 3 tables in Libre Office Base

#Table1: Date, Site, Feeder, RFIDold, ColorBands, SilverBands, Sex, WingLength, Mass_banding, BID, Maturity

#Table 2: Old RFID, New RFID, DateOld, Site

#Table 4: RFID, Notes

#Pseudocode:
#	InFileName = "SagehenBandingFile_recent-version"
#   InFile = open(InFileName, 'r')
#	OutFileName = "Tb1" #Repeat for all 3 files
#	OutFile = open 3 output files

#	for Line in InFile:
		#remove header, store as string
		#strip and 
		#ElementLIst = split
		#RFID = ElementList[x] #repeat for every field I want
		#write.out(headers) #repeat to each output file for each table
		#write.out(data fields) #repeat to each output file for each table

#InFile.close()
#OutFile.close() #repeat all 3 files

#open in files and output files
InFileName = "SagehenBandingData_2019_1004_combined_clean.csv"
InFile = open(InFileName, 'r')

OutFileName1 = "tb1_banding_db.csv"
OutFileName2 = "tb2_RFID_db.csv"
OutFileName4 = "tb4_notes_db.csv"

OutFile1 = open(OutFileName1, 'w')
OutFile2 = open(OutFileName2, 'w')
OutFile4 = open(OutFileName4, 'w')

#create headers for outfiles
OutFile1.write("Date,Site,Feeder,RFID,ColorBands,SilverBands,Sex,WingLength,Mass,BID,Maturity\n")
OutFile2.write("RFID_old,RFID_new,Date_old,Site\n")
OutFile4.write("RFID,Site,Notes\n")


#Parse data from InFile - Sagehen Banding Data - to create tables 1, 2, 4
LineNum = 0
for Line in InFile:
	if LineNum > 0:
		Line = Line.strip('\n')
		ElementList = Line.split(',')

		#capture data
		Site = ElementList[0]
		Date = ElementList[1]
		ColorBands = ElementList[2]
		SilverBands = ElementList[3]
		RFIDold = ElementList[4]
		RFIDnew = ElementList[5]
		Mass_banding = ElementList[6]
		WingLength = ElementList[7]
		BID = ElementList[8]
		Feeder = ElementList[9]
		Sex = ElementList[10]
		Maturity = ElementList[11]
		PreviousHist = ElementList[12]
		Notes = ElementList[13]

		#create tables as outfiles
		TB1 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (Date, Site, Feeder, RFIDold, ColorBands, 
			SilverBands, Sex, WingLength, Mass_banding, BID, Maturity)
		OutFile1.write(TB1)
		
		#only print entries with new RFID to table 2
		if (RFIDnew != ''):
			TB2 = "%s,%s,%s,%s\n" % (RFIDold, RFIDnew, Date, Site)
			OutFile2.write(TB2)

		#only print entries with previous history or notes to table 4
		if (PreviousHist != '' or Notes != ''):
			if (PreviousHist == ''):
				HistNotes = Notes
			if (Notes == ''):
				HistNotes = PreviousHist
			if (Notes != '' and PreviousHist != ''):
				HistNotes = "%s;%s" % (PreviousHist, Notes)
			TB4 = "%s,%s,%s\n" % (RFIDold, Site, HistNotes)
			OutFile4.write(TB4)
	LineNum += 1


InFile.close()
OutFile1.close()
OutFile2.close()
OutFile4.close()
