# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        #edited port and pass to reflect my instance of mongodb
        #USER = 'aacuser'
        #PASS = 'aacpass'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32832
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary 
            self.collection.insert_one(data)
            if insert != 0:
                return True
            else:
                return False
                
        else:
            raise Exception("Nothing to save, because data parameter is empty")
# Create method to implement the R in CRUD.
    def read(self,criteria):
        if criteria is not None: 
            data = self.database.animals.find(criteria)
        else:
            data = self.database.animals.find({})
        return data
# Create method to implement the U in CRUD.
    def update(self, data, updatedData):
        if data and updatedData is not None: 
            updated = self.database.animals.update_many(data,{"$set":updatedData})
        else:
            raise Exception("Nothing to update, data parameter is empty")
        return updated.modified_count
# Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None: 
            deleted = self.database.animals.delete_many(data)
        else:
            raise Exception("Nothing to delete, data parameter is empty")
        return deleted.deleted_count