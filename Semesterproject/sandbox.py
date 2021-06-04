
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import requests
from datetime import datetime
from datetime import timedelta
import time
import json

from pymongo.errors import OperationFailure, DuplicateKeyError

pd.set_option('precision', 2)
pd.set_option('max_rows', 20)
pd.set_option('max_colwidth', 30)
# pd.describe_option('max_rows')
# pd.describe_option('precision')
# pd.describe_option('max_colwidth')


# try:
#     conn =MongoClient(host="mongo",username ="root", password="example")
#     try:
#         conn.server_info()
#         print("Connection Successfull")
#     except OperationFailure as e:
#         return e
# except Exception as e:
#     return e
#
# print (dbConnect())
client = MongoClient(host="localhost",port=27017,username ="root", password="example")
database = client["bdl03"]
# collection_submissions = database['submissions']



# # Get Bulk load of Reddit submissions


# ## 1. Create method for api call

def get_pushshift_data(data_type, **kwargs):
    """Get data from pushshift api -> Reddit
    param p1: String -> "comment" or "submission"
    param p2: Object -> parameters defined in 2.
    return: json file
    """
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    if request.status_code == 200:
        return request.json()
    else:
        return {}

def get_submission_comment_ids(sub_id):
    url = f"https://api.pushshift.io/reddit/submission/comment_ids/{sub_id}"
    request = requests.get(url)
    if request.ok:
        return request.json()
    else:
        return None

def get_comments(comment_ids):
    url = f"https://api.pushshift.io/reddit/comment/search?ids={comment_ids}"
    request = requests.get(url)
    if request.ok:
        return request.json()
    else:
        return None


# ## 2. Define parameters for api call
path = "C:/Users/annam/OneDrive/Documents/dev/MSC/BDL1/Semesterproject"
data_type = "submission"
query="Netflix"
size=500 #500 is max
sort_type="created_utc"
sort="desc"
aggs="created_utc"
fields = ["subreddit",
         "subreddit_id",
         "title",
         "created_utc",
         "permalink",
         "id",
         "num_comments",
         "num_crossposts",
         "score",
         "upvote_ratio"]

subreddits = ["WallStreetBets"]
for subreddit in subreddits:

    # bulk_df = pd.DataFrame()
    current_timestamp = time.time()
    dynamic_timestamp = current_timestamp - (60 * 60 * 24 * 730) #two years ago #(60*60*24)#
    while int(dynamic_timestamp) < int(current_timestamp):
        data = get_pushshift_data(data_type=data_type,q=query,after=int(dynamic_timestamp),sort_type="created_utc",sort="Asc",
                                      fields=fields,size=size,subreddit=subreddit)
        # df = pd.json_normalize(data['data'])
        df = data["data"]
        if len(df) > 0:
            dynamic_timestamp = max([x['created_utc'] for x in df]) + 1
            submission_ids = []
            for element in df:
                try:
                    json_el = json.loads(json.dumps(element))
                    database.submissions.insert_one(json_el)
                    print(f"insertet submission {json_el['id']}")
                    submission_ids.append(json_el['id'])

                except(DuplicateKeyError):
                    print('Duplicate submission caught')

                for submission_id in submission_ids:
                    comment_ids_data = get_submission_comment_ids(submission_id)
                    if comment_ids_data != None:
                        for d in comment_ids_data['data']:
                            comments_ids = str(d)
                            comments = get_comments(comments_ids)
                            try:
                                json_comment = json.loads(json.dumps(comments['data'][0]))
                                json_comment["submission_id"] = submission_id
                                json_comment["_id"] = json_comment["id"]
                            except TypeError:
                                print("Comment id {} returned None Comment was {}".format(d, comments))
                            # database.comments.insert_one(json_el)
                            # print(f"insertet comment")
                            try:
                                database.comments.insert_one(json_comment)
                                print(f"insertet comment")
                            except(DuplicateKeyError):
                                print(f'Duplicate comment caught: {DuplicateKeyError}')
                        print(f"Done with comments of submission {submission_id}")



    else:
            print("done...")
            break;

    #parse date
    # bulk_df["created_utc"] = pd.to_datetime(bulk_df["created_utc"], unit="s", errors='ignore')


    #get latest date for file name #why do i need to convert it again?!
    # latestDate = pd.to_datetime(max(bulk_df["created_utc"]))
    #write to csv
    # bulk_df.to_csv(path+"/submissions/Reddit_BULK_{}_Netflix_{}.csv".format(subreddit,latestDate.strftime('%Y%m%d')), sep=",", index=False)
