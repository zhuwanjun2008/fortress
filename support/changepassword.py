#!/usr/bin/python
#coding=utf-8

import sys
import pexpect
import random

def changepassword(username,sudopasswd):
    
    #生成12位随机字符串作为新密码
    newpassword = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890',16))
    commandline = 'sudo passwd ' + username
    
    child = pexpect.spawn(commandline)
    #关闭脚本执行过程中的输出信息
    #child.logfile = sys.stdout   
    
    child.expect('password for admin:')
    child.sendline(sudopasswd)

    child.expect('New password:')
    child.sendline(newpassword)
    
    child.expect('Retype new password:')
    child.sendline(newpassword)
    child.expect('passwd: all authentication tokens updated successfully.')
    
    return newpassword


if __name__ == '__main__':
    try:
        newPassword =  changepassword('用户名','sudo 密码')
        print "IP:xxx.xxx.xxx.xxx"
        print "Port:端口"
        print "UserName:用户名"
        print "NewPassword: %s" %(newPassword)
    except Exception,e:
        print(str(e))
        print 9999
    
