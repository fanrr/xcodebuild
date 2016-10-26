# -*- coding: utf-8 -*-
import optparse
import os
import sys
import getpass
import json
import hashlib

# mainPath="/Users/Raymond/Documents/kukeLive/KukerLive"
# targetName="KukerLive"
# schemeName="KukerLive"
# certificateName="iPhone Developer: Lei Gao (7BD2GN9H2M)"
# exportPath="/Users/Raymond/Desktop"
# configName="config.json"
# configDirName=".build_app_json"
mainPath        = None
targetName      = None
schemeName      = None
certificateName = None
exportPath      = None
configName      = "config.json"
configDirName   = ".build_app_json"
commendPath     = "/Users/" + getpass.getuser()
#显示已有的参数
def showParameter():
    print "=================================="
    print "mainPath          :%s"%mainPath
    print "targetName        :%s"%targetName
    print "schemeName        :%s"%schemeName
    print "certificateName   :%s"%certificateName
    print "exportPath        :%s"%exportPath
    print "=================================="
    pass


#设置参数
def setParameter():
    global mainPath
    global targetName
    global schemeName
    global certificateName
    global exportPath
    mainPath        =raw_input("input mainPath:")
    targetName      =raw_input("input targetName:")
    schemeName      =raw_input("input schemeName:")
    certificateName =raw_input("input certificateName:")
    exportPath      =raw_input("input exportPath:")

    showParameter()
    #保存到本地
    try:
        fout = open(commendPath + "/" + configDirName + "/" + configName,'w')
        config = {}
        config["mainPath"]        =mainPath
        config["targetName"]      =targetName
        config["schemeName"]      =schemeName
        config["certificateName"] =certificateName
        config["exportPath"]     =exportPath
        outStr = json.dumps(config,ensure_ascii = False)
        fout.write(outStr.strip().encode('utf-8') + '\n')
        fout.close()
    except Exception,e:
        print Exception
        print e
    pass

def configAction():
    if not os.path.exists(commendPath + "/" + configDirName):
        os.system("cd %s;mkdir %s"%(commendPath,configDirName))
    if not os.path.isfile(commendPath + "/" + configDirName + "/" + configName):
        os.system("cd %s;touch %s"%(commendPath + "/" + configDirName,configName))
        initConfig()
    pass
def initConfig():
    fout = open(commendPath + "/" + configDirName + "/" + configName,'w')
    config = {}
    config["mainPath"]        = None
    config["targetName"]      = None
    config["schemeName"]      = None
    config["certificateName"] = None
    config["exportPath"]      = None
    outStr = json.dumps(config,ensure_ascii = False)
    fout.write(outStr.strip().encode('utf-8') + '\n')
    fout.close()
    pass

def readJsonFile():
    fin = open(commendPath + "/" + configDirName + "/" + configName,'r')
    for eachLine in fin:
        line = eachLine.strip().decode('utf-8')
        line = line.strip(',')
        js = None
        try:
            js = json.loads(line)
            global mainPath
            global targetName
            global schemeName
            global certificateName
            global exportPath

            mainPath=js["mainPath"]
            targetName=js["targetName"]
            schemeName=js["schemeName"]
            certificateName=js["certificateName"]
            exportPath=js["exportPath"]
        except Exception,e:
            print Exception
            print e
            continue
    fin.close()
    pass

def isNone(para):
    if para == None or len(para) == 0:
        return True
    else:
        return False
    pass
#是否需要设置参数
def isNeedSetParameter():
    if isNone(mainPath) or isNone(targetName) or isNone(schemeName) or isNone(certificateName) or isNone(exportPath):
        return True
    else :
        return False

def cleanAction():
    action="cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean"%(mainPath,targetName,schemeName)
    print(action)
    os.system(action)
    pass

def buildAction():
    action="cd %s;xcodebuild \
    -workspace %s.xcworkspace \
    -scheme %s CODE_SIGN_IDENTITY='%s' \
    -derivedDataPath build/"%(mainPath,targetName,schemeName,certificateName)
    print(action)
    os.system(action)
    pass

def creatAction():
    action="cd %s;xcrun -sdk iphoneos PackageApplication \
    -v %s/build/Build/Products/Debug-iphoneos/%s.app \
    -o %s/KukerLive.ipa \
    CODE_SIGN_IDENTITY='%s'"%(mainPath,mainPath,targetName,exportPath,certificateName)
    print(action)
    os.system(action)
    pass

#删除文件夹
def rmoveFinder():
    path=mainPath + "/build"
    print(path)
    os.system("rm -r -f %s"%path)
    pass


def main():
    os.system("clear")
    configAction()
    readJsonFile()
    if isNeedSetParameter():
        print "您需要设置参数,您的参数如下:"
        showParameter()
        setParameter()
        sys.exit()
    # cleanAction()
    # buildAction()
    # creatAction()
    rmoveFinder()
    return
main()
