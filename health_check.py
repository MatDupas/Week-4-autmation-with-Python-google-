#!/usr/bin/env python3

import psutil
import socket
import email.message
import smtplib


def check_cpu_ok():
    '''retruns false if CPU usage is over 80%'''
    return psutil.cpu_percent(1) < 80

def disk_space_ok():
    '''Report an error if available disk space is lower than 20%'''
    return (psutil.disk_usage('/').percent) > 20

def memory_ok():
    '''Report an error if available memory is less than 500MB'''
    return psutil.virtual_memory().free > 500*1024*1024


def network_ok():
    '''Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"'''
    hostname = socket.gethostbyname('localhost')
    return hostname == "127.0.0.1"


def send_email(sender, recipient, subject, body):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()



if __name__ == "__main__":
    if not check_cpu_ok():
        send_email('automation@example.com','student-03-2b068cbe729c@example.com',
                 'Error - CPU usage is over 80%','Please check your system and resolve the issue as soon as possible.')
    elif not disk_space_ok():
        send_email('automation@example.com','student-03-2b068cbe729c@example.com',
        'Error - Available disk space is less than 20%','Please check your system and resolve the issue as soon as possible.')
    elif not memory_ok():
        send_email('automation@example.com','student-03-2b068cbe729c@example.com',
        'Error - Available memory is less than 500MB','Please check your system and resolve the issue as soon as possible.')
    elif not network_ok():
        send_email('automation@example.com','student-03-2b068cbe729c@example.com',
        'Error - localhost cannot be resolved to 127.0.0.1','Please check your system and resolve the issue as soon as possible.')
    else: 
        print("Everything is fine !")
