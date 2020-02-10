# import otpRequest as otp

# OTP = otp.getOTP()
# userOTP = input('Enter OTP: ')
# if(OTP == userOTP):
# 	print('Successfully logged in!')
# else:
# 	print('Invalid OTP!')
import xml.etree.ElementTree as ET
import os
OTP = os.system("gcc ~/Sruthi/OTP.c")
print(OTP)
tree = ET.parse('configurations.xml')
root = tree.getroot()
for configurationFile in root:
	for line in configurationFile:
		print(line.text)
	# if(line.attrib['key'] == 'Update'):