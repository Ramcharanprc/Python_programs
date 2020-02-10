# Method two for inserting data to a xml file.
import xml.etree.ElementTree as ET
fileName = 'data.xml'
tree = ET.parse(fileName)
root = tree.getroot()
# items = ET.Element('items')
# item1 = ET.Element('item1')
# item2 = ET.Element('item2')
# item1.text = 'Pen'
# item2.text = 'Book'
# root.insert(0, items)
# root.insert(1, item2)
# root.insert(1, item1)
# data = ET.ElementTree(root)
# data.write('data.xml')
confirmation = 'y'
while (confirmation == 'y'):
	items = ET.Element('items')
	itemName = ET.Element('itemName')
	itemPrice = ET.Element('itemPrice')
	itemQuantity = ET.Element('itemQuantity')
	itemName.text = input('Enter Item name: ')
	itemPrice.text = input('Enter Item Price: ')
	itemQuantity.text = input('Enter Item quantity: ')
	root.insert(0, items)
	items.insert(0, itemQuantity)
	items.insert(0, itemPrice)
	items.insert(0, itemName)
	data = ET.ElementTree(root)
	data.write(fileName)
	confirmation = input('Do you want to insert another item details? (y or n) ')

