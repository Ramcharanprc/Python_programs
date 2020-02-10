import requests
import random
import json
import sys
try:
	URL = 'https://www.sms4india.com/api/v1/sendCampaign'
	# MobileNumber = sys.argv[1]
	OTP = str(random.randint(100000, 999999))
	OTPMessage = OTP + ' is your OTP.' 
	 # OTPMessage = OTP + 'is your OTP. Please DO NOT share this with anyone.'
	req_params = {
	'apikey':'DUMD3TFO6POH2TI1JMIKVNSNOSBHPDL7',
	'secret':'AMF87OIXSEA5OZ1Y',
	'usetype':'stage',
	'phone': 9441957221,
	'message':OTPMessage,
	'senderid':'Ram'
	}
	response = requests.post(URL, req_params)
	print(response.json())
	# print('OTP sent to the registered mobile number.')
	# with open('generatedOTP.cfg', 'w') as fpFile:
	# 	fpFile.write(OTP)
except IndexError:
	print('Argument is missing!')
