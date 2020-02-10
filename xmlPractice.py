# Creating XML file and writing data into that file.
import xml.etree.ElementTree as ET
confirmation = 'y'
fileName = 'employee.xml'
tree = ET.parse()
tecnics = tree.getroot(fileName)
while (confirmation == 'y'):
	employee = ET.SubElement(tecnics, 'employee')
	employeeId = ET.SubElement(employee, 'employeeId', Status = 'A').text = input('Enter Employee Id: ')
	employeeName = ET.SubElement(employee, 'employeeName').text = input('Enter Employee Name: ')
	employeecontact = ET.SubElement(employee, 'employeeContact').text = input('Enter Contact Number: ')
	# employeeId.set('Status', 'A')
	data = ET.ElementTree(tecnics)
	data.write(fileName)
	confirmation = input('Do you want to add one more Employee details? (y or n) ')
# for record in tecnics:
	# print(len(record))
	# for detail in record:
	# 	print(detail.tag, detail.text)
	# print()