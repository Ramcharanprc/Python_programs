# Framework using SQLite.
import sqlite3

active = 'A'
inactive = 'I'
status = 'Status'
connection = sqlite3.connect('Ram.db')
generalTable = connection.execute('select * from general_configurations')
menuConfigurations = []


def getGeneralConfigurationValue(configurationkey):
	return generalConfigurations[configurationkey]

def getRecord(Id):
	data = connection.execute('select * from ' + dataTableName + ' where ' + columnNames[0] + ' = ' + Id + ' and ' + columnNames[-1] + ' = "' + active + '"')
	record = data.fetchall()
	if(len(record) != 0):
		for line in record:
				printRecord(line)
	else:
		print(getGeneralConfigurationValue('IdNotFound'))
		printNewLine()
		showMenu()

def printNewLine():
	print()

def printRecord(record):
	for (fieldName, fieldValue) in zip(fieldConfigurations, record):
			if(fieldName != status):
				print(fieldName + ': ' + str(fieldValue))

def create():
	printNewLine()
	print(getGeneralConfigurationValue('Create'))
	query = 'insert into ' + dataTableName + ' values ("'
	for field in fieldConfigurations:
		if(field != status):
			userInput = input(field + ": ")
			query = query + userInput + '", "' 
		else:
			query = query + active + '")'
	connection.execute(query)
	connection.commit()
	print(getGeneralConfigurationValue('Created'))
	printNewLine()

def view():
	data = connection.execute('select * from ' + dataTableName + ' where ' + columnNames[-1] + ' = "' + active + '"')
	printNewLine()
	print(getGeneralConfigurationValue('View'))
	for record in data:
		printRecord(record)
		printNewLine()

def update():
	printNewLine()
	print(getGeneralConfigurationValue('Update'))
	userId = input('Enter ' + fieldConfigurations[0] + ': ')
	printNewLine()
	getRecord(userId)
	printNewLine()
	for counter in range(1, len(fieldConfigurations)):
		if (fieldConfigurations[counter] != status):
			print(str(counter) + ') ' + fieldConfigurations[counter])
	userChoice = int(input(getGeneralConfigurationValue('Choice') + ': '))
	updateValue = input(fieldConfigurations[userChoice] + ': ')
	connection.execute('update ' + dataTableName + ' set ' + columnNames[userChoice] + ' = ' + updateValue + ' where ' + columnNames[0] + ' = ' + userId)
	connection.commit()
	print(getGeneralConfigurationValue('Updated'))
	printNewLine()

def delete():
	printNewLine()
	print(getGeneralConfigurationValue('Delete'))
	userId = input('Enter ' + fieldConfigurations[0] + ': ')
	printNewLine()
	getRecord(userId)
	printNewLine()
	confirmation = input(getGeneralConfigurationValue('Confirmation') + ': ')
	if(confirmation == 'y'):
		connection.execute('update ' + dataTableName + ' set ' + columnNames[-1] + ' = "' + inactive + '" where ' + columnNames[0] + ' = ' + userId)
		connection.commit()
		print(getGeneralConfigurationValue('Deleted'))
		printNewLine()

def search():
	printNewLine()
	print(getGeneralConfigurationValue('Search'))
	userId = input('Enter ' + fieldConfigurations[0] + ': ')
	printNewLine()
	getRecord(userId)
	printNewLine()

def exitProgram():
	exit()

def showMenu():
	while True:
		for line in menuConfigurations:
			print(line)
		userChoice = int(input(getGeneralConfigurationValue('Choice') + ': '))
		if(userChoice > 0 and userChoice < 7):
			[create, view, update, delete, search, exitProgram][userChoice - 1]()
		else:
			

with open('menu.cfg') as fpFile:
	for lineWithNewLine in fpFile:
		lineWithoutNewLine = lineWithNewLine.replace('\n', '')
		menuConfigurations.append(lineWithoutNewLine)
generalConfigurations = {}
for line in generalTable:
	generalConfigurations[line[0]] = line[1]

dataTableName = generalConfigurations['DataTableName']
pragmaQuery = 'pragma table_info("' + dataTableName + '")'
fieldDetails = connection.execute(pragmaQuery)
fieldConfigurations = []
columnNames = []
for line in fieldDetails:
	columnNames.append(line[1])
	text = line[1].replace('_', ' ')
	fieldConfigurations.append(text)
showMenu()
