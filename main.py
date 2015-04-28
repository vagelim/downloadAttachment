#!/usr/bin/python
from handler import *

USERNAME = 
PASSWORD = 


def main():
	m = loginMail(USERNAME, PASSWORD)
	try:
		mail = readMail(m, checkMsgNum(m))
	except:
		print 'No new mail'
		return 'No new mail'
	sender = querySender(mail)
	if sender in AUTHORIZED:
		filename = getAttachment(mail)
	else:
		filename = 'Invalid Sender'
		raise Exception('Invalid Sender')

	response = []
	response.append(sender)
	response.append(filename)
	return response
	
if __name__ == '__main__':
	main()
