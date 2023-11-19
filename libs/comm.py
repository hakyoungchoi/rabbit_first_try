import json
import mojito

def get_config():
    with open("./config.json", "rt", encoding="UTF8") as settings : 
        return json.load(settings)

def get_broker(): 
    broker = mojito.KoreaInvestment(
            api_key='PSKDWCxqtcDGeqhksBpJzoaYGXm6j8Ij7uyK',
            api_secret='RJNGIWf1PxqLEixGeahywHk+yopNtfHTdFZkr1jQPS0tZTP9GLKdKD+HhSzm2y6zPSZ806gKvtI8aszFYAb/uifwO8dYZytMeh+//JL3uKhHMXNHhLLCMcFr6OvtnqjvUgChPheCsaEVBmr64c+5GKsz28yEnRuQbgAUCLEKqPksfgpmb6A=',
            acc_no='69447656-01'
            )
    return broker
    