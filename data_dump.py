import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    #conver dataframe to json format so that we can dump these record in mongo DB
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())#json.load is used to convert any python object
    print(json_record[0])

    #insert converted json record to mongo DB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



