# Framework of CRUD functions in Python.
menu = 'menu.cfg'
fields = 'fields.cfg'
generalFile = 'general.cfg'
dataFile = 'data.dat'
active = 'A'
inactive = 'I'
configurationFiles = []
allRecords = []

def getRecordAndRecordPosition():
	IdValue = input(configurationFiles[2]['Id'] + ': ')
	try:
		for (record, recordCounter) in zip(allRecords, range(0, len(allRecords))):
			if record[-1] == 'A' and record[0] == IdValue:
				recordCount = recordCounter
				recordFound = record
				break
		return recordFound, recordCount
	except:
		printGeneralConfigurationValue('IdNotFound')
		printNewLine()
		showMenu()

def getConfigurationFile(fpFile):
	fileToList  = []
	with open(fpFile) as ptrFile:
		for lineWithNewLine in ptrFile:
			lineWithoutNewLine = lineWithNewLine.replace('\n', '')
			fileToList.append(lineWithoutNewLine)
	configurationFiles.append(fileToList)

def displayFieldNamesAndFieldValues(record):
	for(fieldName, fieldValue) in zip(configurationFiles[1], record):
		print(fieldName + ': ' + fieldValue)

def printFieldNamesAndFieldValuesOnPaper(record):
	with open('/dev/ttyACM0') as fpPrint:
		fpPrint.write(displayFieldNamesAndFieldValues(record))

def printGeneralConfigurationValue(configurationKey):
	print(configurationFiles[2][configurationKey])

def printNewLine():
	print()

def writeDataToFile(records):
	with open(dataFile, 'w') as fpDataFile:
		fpDataFile.write(str(records))

def create():
	printNewLine()
	printGeneralConfigurationValue('Create')
	printNewLine()
	record = []
	for fieldLine in configurationFiles[1]:
		record.append(input(fieldLine + ': '))
	record.append('A')
	allRecords.append(record)
	writeDataToFile(allRecords)
	printGeneralConfigurationValue('Details')
	printNewLine()

def view():
	printNewLine()
	printGeneralConfigurationValue('View')
	printNewLine()
	if len(allRecords) != 0:
		for record in allRecords:
			if record[-1] == 'A':
				displayFieldNamesAndFieldValues(record)
				printNewLine()
	else:
		printGeneralConfigurationValue('notCreated')
		printNewLine()

def update():
	printNewLine()
	printGeneralConfigurationValue('Update')
	IdName = configurationFiles[1][0]
	record, recordCounter = getRecordAndRecordPosition()
	displayFieldNamesAndFieldValues(record)
	printNewLine()
	for (fieldName, counter) in zip(configurationFiles[1], range(0, len(configurationFiles[1]))):
		if fieldName != IdName:
			print(str(counter) + ') ' + fieldName)
	userChoice = int(input(configurationFiles[2]['Choice'] + ': '))
	allRecords[recordCounter][userChoice] = input(str(configurationFiles[1][userChoice]) + ': ')
	writeDataToFile(allRecords)
	printGeneralConfigurationValue('Updated')
	printNewLine()

def delete():
	printNewLine()
	printGeneralConfigurationValue('Delete')
	record, recordCounter = getRecordAndRecordPosition()
	printNewLine()
	displayFieldNamesAndFieldValues(record)
	printNewLine()
	userConfirmation = input(configurationFiles[2]['Confirmation'])
	if userConfirmation == 'y':
		allRecords[recordCounter][-1] = inactive
		printGeneralConfigurationValue('Deleted')
	writeDataToFile(allRecords)
	printNewLine()

def search():
	printNewLine()
	printGeneralConfigurationValue('Search')
	printNewLine()
	record, recordCounter = getRecordAndRecordPosition()
	if (int(input('1) Display on moniter.\n2) Print on a paper.\nEnter your choice:')) == 2):
		printFieldNamesAndFieldValuesOnPaper(record)
	else:
		displayFieldNamesAndFieldValues(record)
	printNewLine()

def exitProgram():
	printGeneralConfigurationValue('ThankYou')
	exit()

def showMenu():
	while True:
		for menuLine in configurationFiles[0]:
			print(menuLine)
		userChoice = int(input(configurationFiles[2]['Choice'] + ': '))
		if userChoice in range(1, 7):
			[create, view, update, delete, search, exitProgram][userChoice - 1]()
		else:
			printGeneralConfigurationValue('Invalid')			
			printGeneralConfigurationValue('enterValid')
			printNewLine()

getConfigurationFile(menu)
getConfigurationFile(fields)
with open(generalFile) as ptrFile:
	generalFile = {}
	for lineWithNewLine in ptrFile:
		lineWithoutNewLine = lineWithNewLine.replace('\n', '')
		(key, value) = lineWithoutNewLine.split(':')
		generalFile[key] = value
	configurationFiles.append(generalFile)
try:
	allRecords = eval(open(dataFile).readline())
except:
	writeDataToFile('[]')
showMenu()
