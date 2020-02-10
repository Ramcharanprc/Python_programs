# Reading file into a list.
menuConfigurationFile = "bankMenu.cfg"
menuConfigurationList = []
with open(menuConfigurationFile) as menuObject:
	for line in menuObject:
		lineWithNewLine = line.replace('\n', '')
		menuConfigurationList.append(lineWithNewLine)		
for line in menuConfigurationList:
	print(line)
print(menuConfigurationList)
