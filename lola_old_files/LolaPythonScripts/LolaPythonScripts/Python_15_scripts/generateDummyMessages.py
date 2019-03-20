#!/usr/bin/env python
import pika
import sys, random
from appConfig import appConfig
import ujson,uuid
from pprint import pprint
import datetime, collections,hashlib, random
from random import randrange

class generateDummyMessages(object):
    __config = None
    __rabbit_config = None
    __message_config = None

    def __init__(self):
        self.__config = appConfig()
        self.__rabbit_config = self.__config.getConfig('fileingest')
        self.__hydracore = str(self.__rabbit_config['hydracore-url'])
        self.__connection = pika.BlockingConnection(pika.URLParameters(self.__hydracore))
        self.__channel= self.__connection.channel()
        #self.__tempQueueName = 'q_test_inbound_embrace_write'
        self.__alphaChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__numChar =  '0123456789'
        self.__alphaNumDash = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.__alphaNumChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.__alphaChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__alphaCharsLower = 'abcdefghijklmnopqrstuvwxyz'
        self.__numberChars = '0123456789'
        self.__alphaNumUnicodeTestChar="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setFirstName(self):
       return self.randomValue(self.__alphaNumUnicodeTestChar, self.getLength())

    def setMiddleName(self):
       return self.randomValue(self.__alphaNumUnicodeTestChar,self.getLength())
    def setLastName(self):
       return self.randomValue(self.__alphaNumUnicodeTestChar, self.getLength())
    def setGender(self):
       return "{}".format(random.choice(['Male','Female']))
    def setEmployeeSSN(self):
       return self.generateSSN()
    def setMemberSSN(self):
       return self.generateSSN()
    def setPhoneNumber(self):
       return "{}-{}-{}".format(''.join(self.randomValue(self.__numberChars,3)),''.join(self.randomValue(self.__numberChars,3)),''.join(self.randomValue(self.__numberChars,4)))
    def setPhoneNumberIsPreffered(self):
       return self.randomBool()
    def setPhoneNumberIsValid(self):
       return self.randomBool()
    def setEmailAddress(self):
       return "{}@{}.com".format(''.join(self.randomValue(self.__alphaNumUnicodeTestChar,self.getLength()+1)),''.join(self.randomValue(self.__alphaChars,self.getLength())))
    def setEmailIsValidated(self):
       return self.randomBool()
    def setEmailIsAttachmentAllowed(self):
       return self.randomBool()
    def setAddressLine1(self):
       return "{} {} {}".format(''.join(self.randomValue(self.__numberChars,3)),''.join(self.randomValue(self.__alphaChars,self.getLength())),''.join(self.randomValue(self.__alphaChars,self.getLength())))
    def setAddressCity(self):
       return self.randomValue(self.__alphaChars,self.getLength())
    def setAddressState(self):
       return self.randomValue(self.__alphaChars,self.getLength())
    def setAddressZip(self):
       return self.randomValue(self.__numberChars, 5)
    def setAddressisPreffered(self):
       return self.randomBool()
    def setDateofBirth(self):
       return "11/15/1998"


    def generateSSN(self):
	 return "{}-{}-{}".format(''.join(random.SystemRandom().choice(self.__numberChars) for _ in range(3)),
                              ''.join(random.SystemRandom().choice(self.__numberChars) for _ in range(2)),
								''.join(random.SystemRandom().choice(self.__numberChars) for _ in range(4)))
    def randomValue(self,charSet, length):
	 return "{}".format(''.join(random.SystemRandom().choice(charSet) for _ in range(length)))
    def getLength(self):
     return randrange(2,11)
    def randomBool(self):
	 return random.choice([True, False])


    def generateDummyDemoMessages(self):
       demoMessage = {
	   "raaid": str(uuid.uuid4()).replace("-",""),
	   "xreflist": {
		"embrace-individual-id": random.choice([None,"999999"]),
		"employee-ssn": "44",
		"member-ssn": "44"
	     },
	    "app-id": "...",
	    "basic-info": {
		"first-name": self.setFirstName(),
		"middle-name": self.setMiddleName(),
		"last-name": self.setLastName(),
		"preferred-name": self.setFirstName(),
		"suffix": random.choice(['Mr',"MRS","MS"]),
		"date-of-birth": "09/08/05",
		"gender": random.choice(['female','male','unknown']),
		"is-minor-consent": "Yes",
		"is-vip": "LALA",
		"status": random.choice(['active','perm-it-care','hospice','deceased'])
	    }
       }
       #print demoMessage
       return self.publishTestQueue(demoMessage,"demographics")

    def publishTestQueue(self,message, messageType):
        self.__channel.basic_publish(exchange='',
                              routing_key="q_test_inbound_embrace_write",
                              body=ujson.dumps(message), properties = pika.BasicProperties(correlation_id = self.createCorrelationID()))


    def closeChannel(self):
        self.__channel.close()

    def createCorrelationID(self):
        sha384 = hashlib.sha384()
        sha384.update(datetime.datetime.utcnow().isoformat())
        sha384.update("_._._")
        sha384.update(str(random.randint(100000, 999999)))
        return sha384.hexdigest()

testIt = generateDummyMessages()
for i in range(5):
    testIt.generateDummyDemoMessages()















