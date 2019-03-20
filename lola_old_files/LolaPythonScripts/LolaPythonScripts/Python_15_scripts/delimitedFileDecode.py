# -#- coding: utf-8 -*-
"""
 @author: shonaikeLola
"""



import pika
from appConfig import appConfig
import unicodecsv,re, uuid,collections,logging
from jsonMessage import jsonMessage
from decimal import Decimal
from os.path import basename
from pprint import pprint
#from emitMessages.emitMessages import emitMessages
from messageEmitter.messageEmitter import messageEmitter
import dateutil.parser
import sys
import ujson
import datetime,hashlib

messageEmitter.setLogging(fileName="example.log",level=logging.WARN)
class delimitedFileDecode(object):


    def __init__(self):
        self.__errorCannotOpenFile = 'ECANTOPENFILE'
        self.__errorCannotParseFile = 'ECANTPARSEFILE'
        self.__errorNotJsonFile = 'ENOTJSONFILE'
        self.__errorRecordIndexError = 'ERECORDINDEXERROR'
        self.__errorDescRecordIndexError = 'This record does not have all the expected fields.'
        self.__errorTypeError = 'ETYPEERROR'
        self.__errorValueError = 'EVALUEERROR'
        self.__errorKeyError = 'EKEYERROR'
        self.__errorFieldRequiredMissing = 'EMISSINGREQFIELD'
        self.__errorFieldRegexError = 'EFIELDREGEXERROR'
        self.__errorFieldMinLength = 'EFIELDMINLENGTH'
        self.__errorFieldMaxLength = 'EFIELDMAXLENGTH'
        self.__warningMissingField = "WMISSINGREQFIELD"
        self.__maxErrorRecordCount = 1000000
        self.__maxErrorRecordPercent = 0.01
        self.__jobID =str(uuid.uuid4()).replace("-","")
        self.__jobFormat ="delimited"
        self.__jobType= "unspecified"
        self.__emptyField="EmptyField"
        self.__delimeter= None
        self.__tmpInjestID = ["placeholder"]
        self.__decodeFile = "unspecified"
        self.__ignoreTopLine = False
        self.__recordLineCount =0
        self.__errorStatsDict = {}





    def configToFinalMessage(self):
        #This take a Config File and Calls the Proper Decoders to Parse the Files
        try:
          config = sys.argv[1]
          with open(config, "r") as configFile:
            config_reader = ujson.load(configFile)
            self.__delimeter = config_reader["field-delimeter"].encode('utf-8')
            if "max-error-record-count" in config_reader:
              self.__maxErrorRecordCount =config_reader["max-error-record-count"]
            if "max-error-record-percent" in config_reader:
              self.__maxErrorRecordPercent = config_reader["max-error-record-percent"]
            if "job-type" in config_reader:
              self.__jobType = config_reader["job-type"].encode("utf-8")
            if config_reader["ignore-top-lines"] == True:
              self.__ignoreTopLine = True
            demoMessagesDict = self.decodeFile(config_reader["recordset"][0]["fields"], config_reader["recordset"][0]["message-type"])
            eligMessagesDict = self.decodeFile(config_reader["recordset"][1]["fields"], config_reader["recordset"][1]["message-type"])
        except Exception,e:
             print str(e)
        return


    # This Method opens up the File for parsing, and formats one record
    #  to the correct MessageType Format(demographic or eligibility) by calling configtoRecordDict() method
    #Also deals with sending Good Record Messages and Bad Record Messages to Rabbit
    def decodeFile(self, configType, messageType):
        decodeFile = sys.argv[2]
        goodRecordsCount = 0
        badRecordsCount = 0
        errorsList = {}
        try:
         with open(decodeFile, "r") as infile:
            self.__decodeFile = str(basename(decodeFile))
            if self.__ignoreTopLine == True:
                     infile.readline()
            #lineCount =0
            #while lineCount <= 500000:
                #infile.readline()
                #lineCount +=1
            decodeReader = unicodecsv.reader(infile, delimiter=self.__delimeter)
            self.__recordLineCount = 0
            for recordLine in decodeReader:
               #Keep Comment out below for testing
               #if self.__recordLineCount <= 20000:
                 try:
                    self.__errorStatsDict = {}
                    recordValueToConfig = self.getConfigtoRecordDict(recordLine, configType)
                    if recordValueToConfig:
                        self.__recordLineCount +=1
                        if self.__recordLineCount == 1:
                           #print lineCount
                           self.__config = appConfig('config.json')
                           self.__rabbit_config = self.__config.getConfig('fileingest')
                           self.__hydracore = str(self.__rabbit_config['hydracore-url'])
                           self.__hydraServer = self.__rabbit_config['hydracore-server']
                           self.__hydraUserName = str(self.__rabbit_config['hydracore-username'])
                           self.__hydraPassword = str(self.__rabbit_config['hydracore-password'])
                           self.__hydraVhost = str(self.__rabbit_config['hydracore-vhost'])
                           messageEmit = messageEmitter()
                           messageEmit.setPublish(self.__hydraServer,self.__hydraUserName,self.__hydraPassword,self.__hydraVhost,self.__hydracore)
                           messageEmit.setNewJob(self.__decodeFile,self.__jobType,self.__jobFormat)
                           messageEmit.setJobStats("stats.fileread.default.default")

                        if "good-record" in recordValueToConfig:
                           messageEmit.publishMessage('ex_inbound_goodrec', messageType+".member."+self.__jobType+".default",recordValueToConfig["good-record"])
                           goodRecordsCount +=1


                        if recordValueToConfig["actuallyBadRecord"]:
                           badRecordsCount +=1

                        if "bad-record" in recordValueToConfig:
                           messageEmit.publishMessageDirect('ex_inbound_badrec', messageType+".member."+self.__jobType+".default",recordValueToConfig["bad-record"])




                 except IndexError:
                    pass
                 finally:
                     #messageEmit.addRecordStats(goodRecordCount=goodRecordsCount,badRecordCount=badRecordsCount)
                     for key in self.__errorStatsDict:
                         errorCode = self.__errorStatsDict[key]["error-code"]
                         errorDesc = self.__errorStatsDict[key]["error-desc"]
                         errorCount = self.__errorStatsDict[key]["counts"]
                         messageEmit.addErrorStats(errorCode,errorDesc,errorCount)
                     if self.__recordLineCount % 10000 == 0:
                      print "done", self.__recordLineCount
               #Kept for testing
              # else:
                   #break
                   #self.__recordLineCount +=1
                  # continue

            #Determines if File has the went over the maximum bad records
            #Sends message to exchange if not

            messageEmit.publishFinish()
            totalRecords = goodRecordsCount + badRecordsCount
            print goodRecordsCount, badRecordsCount
            if badRecordsCount < self.__maxErrorRecordCount and badRecordsCount < (self.__maxErrorRecordPercent * totalRecords):
                messageEmit.jobEmit()
            else:
                messageEmit.jobDiscard()
            messageEmit.jobComplete()



        except Exception,e:
            print str(e)


    def getTmpIngestId(self,index):
           try:
                return self.__tmpInjestID[index +1]
           except:
                return "create"



    #This takes one record and calls other Methods to turn it into one message
    #Calls Validations, Transformations and Converts as well to appropiate Data Type
    def getConfigtoRecordDict(self, recordLine, configType):
        recordDict = {"record-source":self.__decodeFile,"job-id":  self.__jobID,"job-format":self.__jobFormat,"job-type":self.__jobType}
        errorList = []
        hasWarning =False
        isBadRecord =False
        for configFieldDict in configType:
            fieldName = str(configFieldDict["field-name"])
            transformations = configFieldDict["transformations"]
            dataType = configFieldDict["data-type"]
            if transformations == {} or transformations == "None":
                pass
            else:

                field = self.transformField(recordLine,fieldName,transformations)
                if isinstance(field, dict):
                    errorList.append(field)
                    errorStat = field["error-code"]+"|"+field["error-desc"]
                    if errorStat in self.__errorStatsDict:
                        self.__errorStatsDict[errorStat]["counts"] += 1
                    else:
                        field["counts"] = 1
                        self.__errorStatsDict[str(errorStat)] = field
                    if field["error-code"].startswith("W"):
                        hasWarning = True
                    if field["error-code"].startswith("E"):
                        isBadRecord = True
                elif field == self.__emptyField:
                    pass
                else:
                    convertedField = self.convertDataTypeField(field, dataType)
                    recordDict[fieldName] = convertedField
        #Once The Config File has decoded the Data file to a dict, it returns it in the appropiate message format
        if hasWarning:
           return {"bad-record":self.makeBadRecord(recordLine,errorList),"good-record":self.createMessage(recordDict),"actuallyBadRecord":isBadRecord}
        elif len(errorList) > 0:
           recordDict.clear()
           return {"bad-record":self.makeBadRecord(recordLine, errorList),"actuallyBadRecord":isBadRecord}
        elif len(errorList) ==0:
           #RecordDict is is good record, returns good record because no error
           return {"good-record":self.createMessage(recordDict),"actuallyBadRecord":isBadRecord}




    def makeBadRecord(self, recordLine, errorsList):
        # badRecord ={"record":null,"errors":[ {"error-code":null,"error-desc":null}]}
        badRecord = {"record-source":self.__decodeFile,"job-id":  self.__jobID,"job-format":self.__jobFormat,"job-type":self.__jobType}
        recordLine = "|".join(recordLine)
        badRecord["record"] = recordLine
        badRecord["errors"] = errorsList
        return badRecord

    #Creates HashID for Fields specified By Config
    def createHashId(self, lst, salt):
        sha1 = hashlib.sha1()
        id = salt.join(lst)
        sha1.update(id)
        return sha1.hexdigest()

    #Transforms the fields specified by Config
    def transformField(self, recordLine,fieldName, transformations):
            transformationsKeysList = sorted(transformations.keys())

            for numKey in transformationsKeysList:
                transformationType = transformations[numKey]["type"]
                if "sha1" in transformationType:
                  salt = transformations[numKey]["salt"].encode('utf-8')
                  fieldPositionList = [recordLine[transformations[numKey]["field-positions"][0]].encode('utf-8'),recordLine[transformations[numKey]["field-positions"][1]].encode('utf-8'),recordLine[transformations[numKey]["field-positions"][2]].encode('utf-8')]
                  field = self.createHashId(fieldPositionList, salt)
                  if fieldName == "xreflist.tmp-injest-id":
                    if self.getTmpIngestId(self.__recordLineCount) != "create":
                      field = self.getTmpIngestId(self.__recordLineCount)
                    else:
                        self.__tmpInjestID.append(field)
                  return field
                if  "default" in transformationType:
                    field = transformations[numKey]["value"]

                if transformationType == "position":
                    position = transformations[numKey]["value"]
                    if isinstance(position,int):
                       field = recordLine[position]
                    elif isinstance(position,list):
                        for i in range(len(position)):
                         if recordLine[int(position[0])] != self.__emptyField:
                            field = recordLine[position[i]]
                if field == "":
                   return self.__emptyField
                if transformationType =="trim":
                     field = field.strip(" ")
                if transformationType == "trimNumber":
                    field =  field.replace("-","")
                    field =  field.replace("(","")
                    field =  field.replace(")","")
                if transformationType == "trimZip5":
                    if field[0:4] == "0000":
                       field = field[4:]
                    if int(field) >= 00500:
                       if len (field) == 5:
                          field = field
                       elif len(field) >5:
                         field = field[0:5]
                       else:
                         field = self.__emptyField
                if transformationType == "trimZip4":
                    if len(field) >5:
                        field = field[5:]

                if transformationType == "lookup":
                     field = field.lower()
                     for key in transformations[numKey]["values"]:
                        if field == key:
                           field = transformations[numKey]["values"][key]
                if transformationType == "stripSuffix":
                    for i in range(len(transformations[numKey]["chars"])):
                       suffixIdx = field.find(transformations[numKey]["chars"][i])
                       if suffixIdx != -1:
                           suffixField = field[suffixIdx:]
                           for j in range(len(transformations[numKey]["values"])):
                               if suffixField.find(transformations[numKey]["values"][j]):
                                   field= suffixField
                                   break
                               else:
                                   field = "N\A"
                       else:
                           field = "N\A"
                if transformationType == "todate":
                    field=str(dateutil.parser.parse(field).isoformat())
                if "isRequired" in transformationType and field == self.__emptyField:
                   return  {"error-code":self.__errorFieldRequiredMissing,"error-desc": fieldName}
                if "isImportant" in transformationType and field == self.__emptyField:
                   return {"error-code":self.__warningMissingField,"error-desc": fieldName}
                if field == self.__emptyField:
                    return field
                if "min-length" in transformationType and len(field) < int(transformations[numKey]["value"]):
                   return {"error-code":self.__errorFieldMinLength,"error-desc": fieldName}
                if "max-length" in transformationType and len(field) > int(transformations[numKey]["value"]):
                   return {"error-code":self.__errorFieldMaxLength,"error-desc": fieldName}
                if "valid-values" in transformationType and field not in transformations[numKey]["valid-values"]:
                   return {"error-code":self.__errorFieldRegexError,"error-desc": fieldName}
                if "regex" in transformationType and not re.search(transformations[numKey]["value"], field, re.UNICODE):
                   return {"error-code":self.__errorFieldRegexError,"error-desc": fieldName}

            return field
            #if "5" in transformations:
                #field = datetime.datetime.utcnow()


    # This takes a mapped record and forms it into the nested Dictionary message format
    def createMessage(self, recordDict):
        messageFormat = jsonMessage()
        maxDepth = messageFormat._jsonMessage__setMaxDepth(recordDict)
        messageConfig = messageFormat.formMessage(recordDict, maxDepth)
        for key in messageConfig:
            if "-list" in key:
                for i in range(len(messageConfig[key])):
                  messageConfig[key] = messageConfig[key][i].values()
        return messageConfig


    # This Converts the data to the right type
    def convertDataTypeField(self, field, dataType):
        if field != self.__emptyField:
            if dataType == "string":
                return field.encode("utf-8")
            if dataType == "unicode":
                return field
            if dataType == "decimal":
                return Decimal(field)
            if dataType == "iso8601":
                return field
            return field



