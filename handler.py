#!/usr/bin/python
# __author__ = 'vageli'

from imaplib import *
import os
import email
path = os.path.dirname(os.path.abspath(__file__)) + '/' #Current path
detach_dir = path

AUTHORIZED = ['vagelim@gmail.com']

#First login
#Check mail
#If new mail exists, check the sender
#If sender is valid, download file

def loginMail(username,password):
    m = IMAP4_SSL("imap.gmail.com")
    if username == None or password == None:
	    raise Exception('User or pass empty')
    t = m.login(username,password)
    #Return mail object if login successuful
    if t[0] == 'OK':
        return m
    else:
        raise Exception('Invalid credentials')

def checkMsgNum(m):
    """Takes a mail object and returns the number of messages"""
    #mboxes = m.list()[1] Show all boxes
    m.select("INBOX")#Select mailbox
    #data = m.search(None, "(FROM \"default@gmail.com\")") Search specific email addy
    #Change "default@gmail.com" in above to a specific email address to enable search from particular user
    items = m.search(None, "(UNSEEN)")
    msgNum = str(items[1]).rsplit(None)[-1].strip('[\']')

    return msgNum
	
	
def getAttachment(mail, directory=detach_dir):#Download attachment to directory & return filename
    """Takes a mail object and optional path to save attachments"""
    filename = []
    for part in mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        att_path = os.path.join(directory, filename)

        if not os.path.isfile(att_path) :
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()

    return filename
	
def readMail(m, msgNum):#Read a particular email
    """Takes a mail object and a specific email requested, returns email"""
    resp, data = m.fetch(msgNum, "(RFC822)")
    email_body = data[0][1]
    mail = email.message_from_string(email_body)
    #temp = m.store(emailid,'+FLAGS', '\\Seen')
    m.expunge()


    return mail

def querySender(mail):
    start = mail["From"].find('<') + 1
    end = mail["From"].find('>')
    username = mail["From"]
    return username[start:end]
	

	
