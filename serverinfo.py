#!/usr/bin/python
#coding=utf-8

import ConfigParser

#返回配置文件中，指定serverid的name和ip
def getserverinfo(serverid,typetag):
    
    #配置文件读取
    conf = ConfigParser.ConfigParser()
    conf.read("serverlist")

    servername = conf.get(serverid, "name")
    serverip = conf.get(serverid, "ip")
    serveruser = conf.get(serverid, "user")
    serverpassword = conf.get(serverid, "password")
    
    if typetag == "name":
        return servername
    elif typetag == "ip":
        return serverip
    elif typetag == "user":
        return serveruser
    elif typetag == "password":
        return serverpassword
    
    else:
        return (servername,serverip,serveruser,serverpassword)
    

#返回服务器列表
def getservername():
    #配置文件读取
    conf = ConfigParser.ConfigParser()
    conf.read("serverlist")
    
    #获取所有server
    serverids = conf.get("server", "id").split(",")
    
    serverinfo=""
    #遍历所有的ServerID
    for serverid in serverids:
        serverinfo = serverinfo + serverid+ "."+getserverinfo(serverid,"name") + "\n"
        
    return serverinfo


#判断服务器序号是否在服务器名列表
def isdst(server_id):
    #配置文件读取
    conf = ConfigParser.ConfigParser()
    conf.read("serverlist")
    
    #获取所有server
    serverids = conf.get("server", "id").split(",")
    
    #遍历所有的ServerID
    for serverid in serverids:
        if server_id == serverid:
            return True
        else:
            continue
        
    return False
