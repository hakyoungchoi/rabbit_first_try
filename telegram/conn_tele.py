from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from libs.comm import get_config
from loguru import logger

tele_config = get_config()['TeleGram']

async def conn_tele() : 
    api_id = tele_config['API_ID']
    api_hash = tele_config['API_HASH']
    user_name = tele_config['USER_NAME']
    client = await TelegramClient(user_name, api_id, api_hash) 
    return client   
    



