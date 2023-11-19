from apscheduler.schedulers.asyncio import AsyncIOScheduler
from singleton.jobs.get_stock_list import get_stock_list

def init_data() -> None :    
    get_stock_list()

def start_scheduler() -> None :
    scheduler = AsyncIOScheduler()
    scheduler.configure(timezone="Asia/Seoul")
    scheduler.add_job(get_stock_list, "interval", seconds = 600, misfire_grace_time=None)
    scheduler.start()

def start_up_event_handler():
    init_data()
    start_scheduler
