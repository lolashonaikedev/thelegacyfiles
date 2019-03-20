#!/usr/bin/env python
import pika
from appConfig import appConfig
import ujson
import datetime, collections,hashlib, random
from asyncElmerExchange import asyncElmerExchange
from asyncElmer import asyncElmer
from parallelQHandler import parallelQHandler
#from parallelQReaderInClass import parallelQReaderInClass
class emitMessages(object):
    __config = None
    __rabbit_config = None
    __message_config = None

    def __init__(self, jobType):
        self.__tempGoodQueueName = self.createQueueID(jobType)
        self.__tempBadQueueName = self.createQueueID(jobType)
        self.__config = appConfig('config.json')
        self.__rabbit_config = self.__config.getConfig('fileingest')
        self.__hydracore = str(self.__rabbit_config['hydracore-url'])
        self.__asyncStats = asyncElmerExchange(self.__hydracore, 'ex_inbound_stats')

    def deleteTempQueue(self):

        connection = pika.BlockingConnection(pika.URLParameters(self.__hydracore))
        channel = connection.channel()
        channel.queue_delete(queue = str(self.__tempGoodQueueName))
        channel.queue_delete(queue = str(self.__tempBadQueueName))
        channel.close()
        connection.close()

    #Starts connection for publishing TmpQueue
    def startAsync(self):
        self.__asyncGood = asyncElmer(self.__hydracore, self.__tempGoodQueueName)
        self.__asyncBad = asyncElmer(self.__hydracore, self.__tempBadQueueName)

    #Publishes to TmpQueue
    def publishGoodTempQueue(self, message):
         self.__asyncGood.publish(ujson.dumps(message))
    def publishBadTempQueue(self, message):
         self.__asyncBad.publish(ujson.dumps(message))

    #def sharedStartHandler(self,shared):
     #   conn = pika.BlockingConnection(pika.URLParameters(self.__hydracore))
     #   channel = conn.channel()
     #   return  {'channel':channel,'conn':conn}

    #The methods goodHandler, badHandler, Send to Exchange, handle moving TmpQueue to Exchange
    def goodHandler(self, channel, message, messageProps):
        tmpBody= ujson.loads(message)
        contract = tmpBody["job-type"]
        if "basic-info" in message:
            routingKey = "demographic.member."+str(contract)+".default"
        if "app-object-id" in message:
            routingKey = "eligibility.member."+str(contract)+".default"
        channel.basic_publish(exchange='ex_inbound_goodrec',
                              routing_key=routingKey,
                              body=message, properties = pika.BasicProperties(correlation_id = self.createCorrelationID(),delivery_mode=2))

    def badHandler(self, channel, message, messageProps):
        tmpBody= ujson.loads(message)
        contract = tmpBody["job-type"]
        if "basic-info" in message:
            routingKey = "demographic.member."+str(contract)+".default"
        if "app-object-id" in message:
            routingKey = "eligibility.member."+str(contract)+".default"
        channel.basic_publish(exchange='ex_inbound_badrec',
                              routing_key=routingKey,
                              body=message, properties = pika.BasicProperties(correlation_id = self.createCorrelationID(),delivery_mode=2))
    def sendToExchange(self):
        #startSendingBad = parallelQReaderInClass(self.__hydracore,self.__tempGoodQueueName)
        #startSendingGood = parallelQReaderInClass(self.__hydracore, self.__tempBadQueueName)
        startSendingBad = parallelQHandler(self.__hydracore)
        startSendingBad.handleMessages(self.__tempBadQueueName,self.badHandler)
        startSendingGood = parallelQHandler(self.__hydracore)
        startSendingGood.handleMessages(self.__tempGoodQueueName,self.goodHandler)


    #def waiting(self):
        #self.__asyncGood.wait()
        #self.__asyncBad.wait()

    #Emit Job Stats Message
    def emitJobMessage(self,jobFormat = None,jobType = None, jobId =None, jobStatus = None, goodRecordsCount = None, badRecordsCount = None, badRecords = None):
        jobMessage = {"job-id": jobId,
                      "job-status": jobStatus,
                      "job-update-ts": datetime.datetime.utcnow().isoformat(),  # UTCNOWDATETIME,
                      "job-format":jobFormat,
                      "job-type":jobType,
                      "stats": {
                          "good-record-count": goodRecordsCount,
                          "bad-record-count": badRecordsCount
                      },
                      "error-stats": badRecords
                      }
        if jobStatus == "started":
           jobMessage["job-start-ts"] = datetime.datetime.utcnow().isoformat()
        if badRecords:
           badRecordStat = collections.Counter(ujson.dumps(badRecords[i]) for i in range(len(badRecords)))
           jobMessage["error-stats"] = dict(badRecordStat)
        self.__asyncStats.publish(['ex_inbound_stats','stats.fileread.default.default',ujson.dumps(jobMessage),self.createCorrelationID()])


    def createCorrelationID(self):
        sha384 = hashlib.sha384()
        sha384.update(datetime.datetime.utcnow().isoformat())
        sha384.update("_._._")
        sha384.update(str(random.randint(100000, 999999)))
        return sha384.hexdigest()

    def createQueueID(self,jobType):
        sha1 = hashlib.sha1()
        sha1.update(jobType)
        sha1.update(datetime.datetime.utcnow().isoformat())
        sha1.update(str(random.randint(100000, 999999)))
        return sha1.hexdigest()
