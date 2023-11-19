import uvicorn
from fastapi import FastAPI
from api.event_handler import start_up_event_handler
from api.routers.stock_controller.stock_router import router as stock_router
from telegram.conn_tele import conn_tele
from loguru import logger
from libs.comm import get_config
from libs.parsing import process_message
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)


tele_config = get_config()['TeleGram']
app =FastAPI()
app.add_event_handler("startup", start_up_event_handler)
app.include_router(stock_router, prefix="/stock", tags=["stock"])

# Create the client and connect
api_id = tele_config['API_ID']
api_hash = tele_config['API_HASH']
user_name = tele_config['USER_NAME']
client = TelegramClient(user_name, api_id, api_hash) 
start_up_event_handler()


#@client.on(events.NewMessage(chats='t.me/richrichmanman'))
@client.on(events.NewMessage(chats='t.me/maddingStock'))
async def my_event_handler(event):
    logger.debug(event.raw_text)
    process_message(event.raw_text)
    
logger.debug("app star")
client.start() 
client.run_until_disconnected()        

# if __name__ == "__main__":    
    
#     uvicorn.run("main:app", host="0.0.0.0", port=9293)