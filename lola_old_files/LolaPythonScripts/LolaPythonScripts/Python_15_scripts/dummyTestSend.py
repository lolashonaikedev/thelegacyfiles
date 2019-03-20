
#import pika
#import sys
import ujson
from appConfig import appConfig
from couchbase.bucket import Bucket
#from parallelQReader import parallelQReader
#from parallelQHandler import parallelQHandler
from parallelQReaderInClass import parallelQReaderInClass




class hydratoCouchbase(object):
    __config = None
    __rabbit_config = None
    __message_config = None

    def __init__(self):
        self.__config = appConfig()
        self.__rabbit_config = self.__config.getConfig('fileingest')
        self.__hydracore = str(self.__rabbit_config['hydracore-url'])
       
        self.__queueName = "q_itinerary_fileextract"
      

    def sharedStartHandler(self):
    
        return Bucket('couchbase://10.23.8.141/default')
        
    def sharedEndHandler(self,shared):
        
        pass

    def messageHandler(self,shared, messageProps, message):
        entry ={}
        message = ujson.loads(message)
        tmpId = message["xreflist"]["tmp-ingest-id"]
        rv = shared.get(str(tmpId),quiet=True)
        if rv.success:
                print "here"
                entry = rv.value

        if "demographic" in str(messageProps):
                entry['demographics'] = message

        else:
             entry['eligibility'] = message

        shared.upsert(tmpId,entry)

    def makeToCouchBase(self):
          self.__asyncBunny = parallelQReaderInClass( self.__hydracore,self.__queueName)
          self.__asyncBunny.handleMessages(self.sharedStartHandler, self.sharedEndHandler, self.messageHandler)
       testIt = hydratoCouchbase()
testIt.makeToCouchBase()

