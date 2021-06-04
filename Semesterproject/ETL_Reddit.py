#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python
# coding: utf-8

# # ETL Pipeline for Reddit submissions
# #### Get submissions of subreddit "WallStreetBets" with following fields:
# ["subreddit","subreddit_id", "title","created_utc","permalink", "id", "num_comments", "num_crossposts", "score","upvote_ratio"]

#import needed libraries
import pandas as pd
import requests
import datetime
import glob
import re
import time
import json


# ## 1. Methods

# ### 1.1 API

def get_pushshift_data(data_type, **kwargs):
    """Get data from pushshift api -> Reddit
    param p1: String -> "comment" or "submission"
    param p2: Object -> parameters defined in 2.
    return: json file
    """
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    if request.ok:
        return request.json()
    else:
        return None


# ### 1.2 latest date of last load

#get latest date of company
def getLatest(files):
    """
    Get latest Date of of last reddit load
    param p1: list -> files as list from one company
    return: max Date of last load (latest submission) as datetime
    """
    dates = [date for file in files for date in re.findall("(\d{8})", file)]
    dates = [datetime.datetime.strptime(str(i), '%Y%m%d') for i in dates]
    if len(dates)> 0:
        return max(dates)
    else:
        return datetime.datetime.fromtimestamp(time.time()) - datetime.timedelta(days=2)


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


# ## 2. Define parameters

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


# ## 3. Get last date of submission in the previous load

#get latest entry of last load
#if we use S3 buckets we need a different algorithm - the approach stays the same
path = "/opt/datalake/raw_data/reddit/"
path = "C:/Users/annam/OneDrive/Documents/dev/MSC/DWL/dwl/"
ending = "submissions/*.csv"
allFiles = glob.glob(path+ending)
# allFiles = glob.glob("C:/Users/annam/OneDrive/Documents/dev/MSC/DWL/dwl/Reddit_Files/*.csv")
# "dwl/Reddit_Files/Reddit_BULK_WallStreetBets_Netflix_20210317031144.csv"
allFiles

subreddits = ["WallStreetBets", "Netflix","Piracy","Movies"]
for subreddit in subreddits:
    #filter the company files
    subredditFiles = list(filter(lambda k: subreddit in k, allFiles))
    #get latest date from file name
    latestDate = getLatest(subredditFiles)
#get latest date and return it in seconds and add 1 so we dont get duplicates -> still getting duplicates resolve below



    new_df = pd.DataFrame()
    current_timestamp = datetime.datetime.fromtimestamp(time.time())
    dynamic_timestamp = latestDate
    if isinstance(dynamic_timestamp, int):
        dynamic_timestamp = datetime.datetime.strptime(str(dynamic_timestamp), '%Y%m%d')
    while dynamic_timestamp < current_timestamp:
        data = get_pushshift_data(data_type=data_type,q=query,after=dynamic_timestamp,sort_type="created_utc",sort="Asc",
                                      fields=fields,size=size,subreddit=subreddit)
        if data != None:
            df = pd.json_normalize(data['data'])
            if len(df) > 0:
                dynamic_timestamp = max(df["created_utc"].values) + 1
                dynamic_timestamp = datetime.datetime.utcfromtimestamp(dynamic_timestamp)
                new_df = new_df.append(df)
            else:
                dynamic_timestamp = dynamic_timestamp+ datetime.timedelta(days=1)
                print("done...")
                # break;



    if len(new_df) > 0:
        new_df["created_utc"] = pd.to_datetime(new_df["created_utc"], unit="s", errors='ignore')
        # get latest date for file name #why do i need to convert it again?!
        latestDateInResponse = pd.to_datetime(max(new_df["created_utc"]))
        # if max date in response is < latestDate from last load dismiss this upload - else save file
        new_df = new_df[new_df['created_utc'] > pd.to_datetime(getLatest(subredditFiles))]
        ids = new_df["id"]
        comments_ids = ""
        for id in ids:
        #     data = get_submission_comment_ids(id)
        #     if data != None:
        #         for d in data['data']:
        #             comments_ids += str(d) + ","
        # comments_ids = comments_ids[:-1]
        # comments = get_comments(comments_ids)
            data = get_submission_comment_ids(id)
            if data != None:
                index = new_df.index
                condition = new_df["id"] == id
                row_index = index[condition]
                new_df.loc[row_index, 'comment_ids'] = str(data['data'])
                for d in data['data']:
                    comments_ids = str(d)
                    comments = get_comments(comments_ids)
                    try:
                        bulk_df = pd.json_normalize(comments['data'])
                        bulk_df["created_utc"] = pd.to_datetime(bulk_df["created_utc"], unit="s", errors='ignore')
                        latest_date = max(bulk_df["created_utc"])
                        submission_id = [id]
                        bulk_df["submission_id"] = submission_id
                        bulk_df.to_csv("/opt/datalake/raw_data/reddit/comments/Reddit_{}_{}_{}.csv".format(subreddit, comments_ids,
                                                                                     latest_date.strftime('%Y%m%d')), sep=",",
                                       index=False)
                    except TypeError:
                        print("Comment id {} returned None Comment was {}".format(d,comments))


        # comments_df = pd.json_normalize(comments['data'])
        # comments_df["created_utc"] = pd.to_datetime(comments_df["created_utc"], unit="s", errors='ignore')
        # latest_date = max(comments_df["created_utc"])
        #
        # comments_df.to_csv(path+"/comments/{}/Reddit_{}_{}.csv".format(subreddit, subreddit, latestDate.strftime('%Y%m%d')), sep=",")
        print("Wrote Comments df")

        new_df.to_csv(path+"/submissions/{}/Reddit_{}_{}.csv".format(subreddit, subreddit, latestDate.strftime('%Y%m%d')), sep=",")
        print("wrote new submissions")
        print("Done :)")
    else:
        print("No new submissions...")
