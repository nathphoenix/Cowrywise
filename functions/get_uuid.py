import pymongo
import uuid
from datetime import datetime, date, time, timedelta
client = pymongo.MongoClient()
client = client['Bloverse_new_rss']
uuid_collection = client['uuid_tables']

def generate_uuid():

    today = datetime.now()
    today_date = datetime.strftime(today, '%Y-%m-%d %H:%M:%S:%f')
    generated_id = uuid.uuid4()
    generated_id = generated_id.hex
    data = {today_date:generated_id, "run_time": today_date}
    insert = uuid_collection.insert_one(data)
    latest_record = uuid_collection.find({}, {"_id":0, "run_time":0} ).sort([("run_time", -1)]) 
    latest_record = [ items for items in latest_record]
    final_dict = {k:v for element in latest_record for k,v in element.items()}
    return final_dict

