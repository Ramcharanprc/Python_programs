# Sending mail using smtp.
import smtplib
import getpass
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
print('Gmail Login.')
senderEmailId = input('Enter Gmail Id: ')
password = getpass.getpass('Enter Password: ')
try:
	session.login(senderEmailId, password)
	recipientEmailId = input('Enter sender Email Id: ')
	message = input('Enter the message: ')
	session.sendmail(senderEmailId, recipientEmailId, message)
	session.quit()
	print('Mail sent seccessfully.')
except :
	print('Invalid Email or Password!')

