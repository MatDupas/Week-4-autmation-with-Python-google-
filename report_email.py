#!/usr/bin/env python3

import email.message
import mimetypes
import os
import smtplib
import reports
import datetime

def generate_email(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()



def generate_paragraph(path):
  paragraph =""
  for file in os.listdir(path):
    with open(os.path.join(path,file),'r') as f:
      text = f.readlines()
      title, weight, desc = text[0],text[1],text[2]
      paragraph += '\n'.join("name:"+title,"weight:"+weight,"\n")
  return paragraph 


if __name__ == "__main__":
    paragraph = generate_paragraph('~/home/student-03-a899d807370d/supplier-data/descriptions')
    today = datetime.datetime.now().strftime("%B %d,%Y")
    
    reports.generate_report('/tmp/processed.pdf', 'Processed Update on '+today, paragraph)
    
    body ="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message= generate_email('automation@example', 'student-03-a899d807370d@35.223.118.227',
                             'Upload Completed - Online Fruit Store', body, '/tmp/processed.pdf'):
    send(message)
