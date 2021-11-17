#!/usr/bin/python3
""" BaseModel class to define all common attributes/ methods for other
classes """
 import uuid
 from datetime import datetime
 import models

 class BaseModel:
     """
     Basemodel instantiation
     """

     def __init__(self, *args, **kwargs):
         """
         Object constructor.
         Attributes:

         id [str] -- UUID generated with python uuid.
         created_at [datetime] -- contains datetimee of the object
         updated_at [datetime] -- contains datetime of the object
         __class__ [str] -- Basemodel class
         """
         if kwargs:
             for key, value in kwargs.items():
                 if key == 'created_at' or key == 'updated_at':
                     value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                     if key != '__class__':
                         setattr(self, key, value)
                     else:
                         self.id = str(uuid.uuid4())
                         self.created_at = atetime.now()
                         self.updated_at = datetime.now()
                         models.storage.nw(self)
    def __str__(self):
        """
        Method that returns string representation
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, str(self.__dict__))
    
    def save(self):
        """
        Method that update attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
        Method that returns a dict containing all key/value of __dict__
        instance
        """
        dic = dict(**self.__dict__)
        dic['__class__'] = type(self).__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

