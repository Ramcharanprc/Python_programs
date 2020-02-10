import requests
import random
import json
import sys
def GetOTP():
	try:
		URL = 'https://www.sms4india.com/api/v1/sendCampaign'
		# MobileNumber = sys.argv[1]
		OTP = str(random.randint(100000, 999999))
		OTPMessage = OTP + ' is your OTP.' 
		 # OTPMessage = OTP + 'is your OTP. Please DO NOT share this with anyone.'
		req_params = {
		'apikey':'W72M3Z2Q4BKQ9SL8IMFUMNJQVAGL0H36',
		'secret':'RWA6EVIMC4G0GF9M',
		'usetype':'stage',
		'phone':7730038314,
		'message':OTPMessage,
		'senderid':'SMSIND'
		}
		response = requests.post(URL, req_params)
		print(response.json())
		return OTP
		# print('OTP sent to the registered mobile number.')
		# with open('generatedOTP.cfg', 'w') as fpFile:
		# 	fpFile.write(OTP)
	except IndexError:
		print('Argument is missing!')
GetOTP()
