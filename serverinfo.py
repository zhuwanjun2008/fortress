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
    
    if typetag == "name":
        return servername
    elif typetag == "ip":
        return serverip
    else:
        return (servername,serverip)
    

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
