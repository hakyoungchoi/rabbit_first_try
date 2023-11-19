from loguru import logger
from singleton.data.dataclass import StockListData, StockData
from libs.comm import get_broker, get_config

def process_message(message): 
    stock_data = text_parsing(message)
    print(stock_data)
    if stock_data.pasrsing_valid : 
        #<StockData strategy:전략A stock_name:주성엔지니어링(036930) order_type:매도 msg_type:접근 target:26450 >  
        broker = get_broker()        
        if stock_data.order_type == "매수" and stock_data.msg_type == "접근" :         
            logger.debug(f'{stock_data.stock_code} / {stock_data.target} / {stock_data.qty}')
            resp = broker.create_limit_buy_order(
                symbol=stock_data.stock_code,
                price=stock_data.target,
                quantity=stock_data.qty
            )
        elif(stock_data.order_type == '매도') and (stock_data.msg_type == "접근"  or stock_data.msg_type == "도달") :             
            i_have, qty = check_if_i_have_target_stock(broker,  stock_data.stock_code)
            logger.debug(f'{stock_data.stock_code} / {stock_data.target} / {qty}')
            if  i_have :
                resp = broker.create_limit_sell_order(
                    symbol=stock_data.stock_code,
                    price=stock_data.target,
                    quantity=int(qty)
                )
            else : resp = stock_data.stock_code
        else : 
            resp = stock_data.order_type


        logger.debug(resp) 
    else : 
        logger.debug(f'pass')

def text_parsing(msg) :
    try : 
        text_list = msg.split("[")        
        strategy_type = text_list[1][:-1]        
        stock_name = text_list[2][:-1]
        order_type = text_list[3][:-1]
        msg_type = text_list[4][:-1]    
        price_list = text_list[5].split(":")        
        price_text = price_list[1]        
        if price_text.find("(") > 0 :        
            target=price_text.split("(")[1]
            target=target.split(")")[0]
        else :         
            target=price_text.split()[0]                     
        stock_data = StockData(strategy_type, stock_name, order_type, msg_type, target, True)
        return stock_data
    except Exception as e : 
        logger.debug(f"not parsing message: {e}")
        return StockData()

def check_if_i_have_target_stock(broker, stock_code):
    resp = broker.fetch_balance()    
    for comp in resp['output1']:
        if (comp['pdno'] == stock_code): 
            if int(comp['hldg_qty']) > get_config()['Money'] // int(comp['pchs_amt']) : 
                return True, get_config()['Money'] // int(comp['pchs_amt'])
            else : 
                return True, int(comp['hldg_qty'])
    logger.debug("not my stock")
    return False, '0'    