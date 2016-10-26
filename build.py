# -*- coding: utf-8 -*-
import optparse
import os
import sys
import getpass
import json
import hashlib

mainPath        = None
targetName      = None
xcworkspaceName = None
schemeName      = None
certificateName = None
exportPath      = None
configName      = "config.json"
configDirName   = ".build_app_json"
commendPath     = "/Users/" + getpass.getuser()

#参数设置
def setOptparse():
    p = optparse.OptionParser()
    #参数配置指令
    p.add_option("--config","-c",action="store_true", default=None,help = "修改配置参数")
    options,arguments = p.parse_args()
    #配置信息
    if options.config == True and len(arguments) == 0 :
        configAction()
    pass

def configAction():
    os.system("clear")
    readJsonFile()
    print "您的参数如下:"
    showParameter()
    setParameter()
    sys.exit()
    pass

#显示已有的参数
def showParameter():
    print "=================================="
    print "mainPath          :%s"%mainPath
    print "targetName        :%s"%targetName
    print "xcworkspaceName   :%s"%xcworkspaceName
    print "schemeName        :%s"%schemeName
    print "certificateName   :%s"%certificateName
    print "exportPath        :%s"%exportPath
    print "=================================="
    pass


#设置参数
def setParameter():
    global mainPath
    global targetName
    global xcworkspaceName
    global schemeName
    global certificateName
    global exportPath
    mainPathTemp        = raw_input("input mainPath:")
    if not isNone(mainPathTemp):
        mainPath        = mainPathTemp
        pass
    targetNameTemp      = raw_input("input targetName:")
    if not isNone(targetNameTemp):
        targetName      = targetNameTemp
        pass
    xcworkspaceNameTemp = raw_input("input xcworkspaceName:")
    if not isNone(xcworkspaceNameTemp):
        xcworkspaceName = xcworkspaceNameTemp
        pass
    schemeNameTemp      = raw_input("input schemeName:")
    if not isNone(schemeNameTemp):
        schemeName      = schemeNameTemp
        pass
    certificateNameTemp = raw_input("input certificateName:")
    if not isNone(certificateNameTemp):
        certificateName = certificateNameTemp
        pass
    exportPathTemp      = raw_input("input exportPath:")
    if not isNone(exportPathTemp):
        exportPath      = exportPathTemp
        pass
    showParameter()
    #保存到本地
    try:
        fout = open(commendPath + "/" + configDirName + "/" + configName,'w')
        config = {}
        config["mainPath"]        = mainPath
        config["targetName"]      = targetName
        config["xcworkspaceName"] = xcworkspaceName
        config["schemeName"]      = schemeName
        config["certificateName"] = certificateName
        config["exportPath"]      = exportPath
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
    config["xcworkspaceName"] = None
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
            global xcworkspaceName
            global schemeName
            global certificateName
            global exportPath

            mainPath=js["mainPath"]
            targetName=js["targetName"]
            xcworkspaceName=js["xcworkspaceName"]
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
    if isNone(mainPath) or isNone(targetName) or isNone(xcworkspaceName) or isNone(schemeName) or isNone(certificateName) or isNone(exportPath):
        return True
    else :
        return False

def cleanAction():
    action="cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean"%(mainPath,xcworkspaceName,schemeName)
    print(action)
    os.system(action)
    pass

def buildAction():
    action="cd %s;xcodebuild \
    -workspace %s.xcworkspace \
    -scheme %s CODE_SIGN_IDENTITY='%s' \
    -derivedDataPath build/"%(mainPath,xcworkspaceName,schemeName,certificateName)
    print(action)
    os.system(action)
    pass

def creatAction():
    action="cd %s;xcrun -sdk iphoneos PackageApplication \
    -v %s/build/Build/Products/Debug-iphoneos/%s.app \
    -o %s/%s.ipa \
    CODE_SIGN_IDENTITY='%s'"%(mainPath,mainPath,targetName,exportPath,targetName,certificateName)
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
    cleanAction()
    buildAction()
    creatAction()
    rmoveFinder()
    return
main()
