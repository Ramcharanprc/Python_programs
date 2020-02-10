import sqlite3
import xml.etree.ElementTree as ET

connection = sqlite3.connect('Ram.db')
tree = ET.parse('configurations.xml')
root = tree.getroot()

for line in root[2]:
	query = 'insert into general_configurations values ("' + line.tag + '", "' + line.text + '");'
	connection.execute(query)
	connection.commit()
connection.close()