import mojito

from singleton.data.dataclass import StockListData

def get_stock_list():    
    broker = mojito.KoreaInvestment(
                api_key='PSKDWCxqtcDGeqhksBpJzoaYGXm6j8Ij7uyK',
                api_secret='RJNGIWf1PxqLEixGeahywHk+yopNtfHTdFZkr1jQPS0tZTP9GLKdKD+HhSzm2y6zPSZ806gKvtI8aszFYAb/uifwO8dYZytMeh+//JL3uKhHMXNHhLLCMcFr6OvtnqjvUgChPheCsaEVBmr64c+5GKsz28yEnRuQbgAUCLEKqPksfgpmb6A=',
                acc_no='69447656-01'
            )
    symbols = broker.fetch_symbols()    
    StockListData(symbols)