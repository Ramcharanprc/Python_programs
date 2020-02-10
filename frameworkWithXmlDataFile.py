# Framework program which containts CRUD functions. Reading and writing data in an XML file.
import xml.etree.ElementTree as ET
# import otpRequest
dataFile = 'data.xml'
active = 'A'
inactive = 'I'

configurationTree = ET.parse('configurations.xml')
configurations = configurationTree.getroot()
dataTree = ET.parse(dataFile)
root = dataTree.getroot()
# generatedOTP = otp.getOTP()
# userOTP = input('Enter OTP: ')
def getRecord:
	userId = input('Enter')

def create():
	print()
	record = ET.SubElement(root, 'record')
	for field in configurations[1]:
		if (field.tag == 'id'):
			ET.SubElement(record, field.tag, status = active).text = input('Enter ' + str(field.text) + ': ')
		else:
			ET.SubElement(record, field.tag).text = input('Enter ' + str(field.text) + ': ')
	data = ET.ElementTree(root)
	data.write(dataFile)
	print()

def view():
	print()
	for record in root:
		for (fieldName, fieldValue) in zip(configurations[1], record):
			print(fieldName.text + ': ' + fieldValue.text)
		print()

def update():

	print()

def delete():
	print()

def search():
	print()

def exitProgram():
	print(getGeneralConfigurationValue('ThankYou'))
	exit()

def getGeneralConfigurationValue(generalConfigurationKey):
	for line in configurations[2]:
		if(line.tag == generalConfigurationKey):
			text = line.text
			break
	return text

def showMenu():
	# if(userOTP == generatedOTP):
	while True:
		for line in configurations[0]:
			print(line.text)
		userChoice = int(input(getGeneralConfigurationValue('Choice') + ': '))
		if(userChoice > 0 and userChoice < 7):
			[create, view, update, delete, search, exitProgram][userChoice - 1]()
		else:
			print(getGeneralConfigurationValue('Invalid'))
			print(getGeneralConfigurationValue('enterValid'))
showMenu()