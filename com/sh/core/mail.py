'''
Created on 25-Sep-2019

@author: impadmin
'''

import smtplib
import traceback


if __name__ == '__main__':
    sender = 'wm-support@impetus.in'
    receivers = ['aditya.singh@impetus.co.in']
    password = 'Orange@1234'
    
    message = """This is a test e-mail message"""
    
    try:
        smtpObj = smtplib.SMTP('survey.impetus.co.in',2525)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message) 
        print("Successfully sent email")        
    except smtplib.SMTPException:
        print("Error: unable to send email")
        traceback.print_exc()