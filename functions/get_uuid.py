import pymongo
import uuid
from datetime import datetime, date, time, timedelta

def generate_uuid():
    client = pymongo.MongoClient()
    client = client['Bloverse_new_rss']
    uuid_collection = client['uuid_tables']

    today = datetime.now()
    today_date = datetime.strftime(today, '%Y-%m-%d %H:%M:%S:%f')

    # Printing random id using uuid1()
    print ("The random id using uuid1() is : ",end="")
    #print (uuid.uuid4())

    generated_id = uuid.uuid4()
    print(generated_id)
    generated_id = generated_id.hex
    data = {today_date:generated_id, "run_time": today_date}
    insert = uuid_collection.insert_one(data)
    latest_record = uuid_collection.find({}, {"_id":0, "run_time":0} ).sort([("run_time", -1)]) 
    latest_record = [ items for items in latest_record]
    final_dict = {k:v for element in latest_record for k,v in element.items()}
    return final_dict

