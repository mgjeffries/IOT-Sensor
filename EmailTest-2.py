# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import sys
sys.path.append('C:\\Users\\MGJEFFRIES\\Dropbox')
import EmailInfoForIOT

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#with open(textfile) as fp:
    # Create a text/plain message
msg = MIMEText("test1")


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of'
msg['From'] = EmailInfoForIOT.fromaddr
msg['To'] = EmailInfoForIOT.toaddrs

# Send the message via our own SMTP server.

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(EmailInfoForIOT.usernm, EmailInfoForIOT.passwrd)
s.send_message(msg)
s.quit()
