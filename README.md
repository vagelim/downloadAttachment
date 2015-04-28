# downloadAttachment
Download attachment to specified directory - validates against users

Requires user to have a valid gmail account

Will not run without the following modifications to main.py:
```
USERNAME = 'YOU@GMAIL.COM'
PASSWORD = 'YOURGMAILPASSWORD'
```
Will not run without the following modifications to handler.py:
```
detach_dir = 'where you want the files'
AUTHORIZED = a list of authorized users
````
