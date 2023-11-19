import pandas as pd 

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else :
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

class BaseDataClass(object):
    data = pd.DataFrame()

    def __init__(self, data):
        cls= type(self)
        cls.data = data
    
    @classmethod
    def get_data(cls):
        return cls.data
        