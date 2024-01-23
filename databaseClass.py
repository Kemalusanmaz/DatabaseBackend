import pymongo

from conf import Configuration as conf

class dBClient: # A database class is made to manage structure

    db = pymongo.MongoClient(conf.connnectionString) # define database server with MongoClient. This works in localhost. db variale can can call with dBclient.db

    def __init__(self,dbName,collectionName):  #there is a initialize method which is taken two argument from out the method
        self.dbName = dbName  #Variables can pass method to method if it defines with self.
        self.collectionName = collectionName
        self.labviewDb = dBClient.db[self.dbName] #this is the part that defines database name
        self.collection = self.labviewDb[self.collectionName] #this is the part that defines collection name
   
    def insertRecord(self,dataResult): # This is a method which manages inserting data to the database. This method takes one argument
        try:
            self.collection.insert_one(dataResult) #dataResult variable is added bt insert_one method. self.collection represent relative collection. 
        except Exception as ex:
            print(ex)
 
    def deleteRecord(self):  #This is a method which delete data in the database.
        try:
            self.collection.delete_many({}) #all data will deleteted with "{}" ann delete_many method is used for this.
            print(f"Collection {self.collectionName} silinmiştir.") #Deleted collection is shown at terminal 
        except Exception as ex:
            print(f"Collection {self.collectionName} silinememiştir.",ex)

    @staticmethod
    def createDB():
        pass
    @staticmethod
    def createCollection():
        pass
    @staticmethod
    def findRecord():
        pass
    @staticmethod
    def filterRecord():
        pass
    @staticmethod
    def updateRecord():
        pass    

