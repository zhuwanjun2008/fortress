#!/usr/bin/python
#coding=utf-8

import smtplib
import datetime
import os
from email.mime.text import MIMEText

def send_mail(mailfrom,mailpassword,mailserver,mailto,sub,content):
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = mailfrom
    msg['To'] = mailto
    
    try:
        server = smtplib.SMTP()
        server.connect(mailserver)
        server.login(mailfrom,mailfrompassword)
        server.sendmail(msg['From'], msg['to'], msg.as_string())
        server.close()
        
        f = open(r'mail.txt', 'a')
        nowtime=datetime.datetime.now()
        f.write(nowtime.strftime("%Y-%m-%d %H:%M:%S:")+'发送成功' + '\n')
        f.close()
        
        return True
    
    except Exception, e:
        f = open(r'mail.txt', 'a')
        nowtime=datetime.datetime.now()
        f.write(nowtime.strftime("%Y-%m-%d %H:%M:%S:")+str(e) + '\n')
        f.close()
        
        return False