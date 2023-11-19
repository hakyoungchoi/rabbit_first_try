import pandas as pd 
from singleton.data.base import BaseDataClass, Singleton
from libs.comm import get_config

class StockListData(BaseDataClass, metaclass=Singleton):
    pass

class StockData : 
    def __init__(self, strategy_type = None, stock_name =None, order_type=None, msg_type=None , target=None, parsing_valid=False):
        self.strategy_type = strategy_type 
        self.pasrsing_valid = parsing_valid
        self.stock_name = stock_name
        self.order_type = order_type
        self.msg_type = msg_type        
        if parsing_valid:
            self.target = int(target)
            self.stock_code = self.get_stock_code(stock_name)
            self.qty = get_config()['Money']//self.target 
    
    def __repr__(self):
        if self.strategy_type != None : 
            return f"strategy:{self.strategy_type} stock_name:{self.stock_name}({self.stock_code}) order_type:{self.order_type} msg_type:{self.msg_type} target:{self.target} "
        else : 
            return f"pass message"

    def get(self):
        return self.stock_name, self.order_type, self.msg_type, self.target

    def get_stock_code(self, stock_name):    
        stock_list = StockListData.data            
        return stock_list[stock_list['한글명'] == stock_name]['단축코드'].iloc[0]

    