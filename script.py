import praw as pr
from praw.models import MoreComments
import pandas as pd

inst=pr.Reddit(client_id='3OfPLZHksCkemA',
                     client_secret='MvF8ObKoHJ8PNAFDh00WdSx8Y9E',
                     password='precogreddit',
                     user_agent='testscript',
                     username='DikshantSagar')

sub=inst.subreddit('india')

flairs=['Politics','Non-Political','AskIndia', "[R]eddiquette", 'Science/Technology', 'Policy/Economy', 'Business/Finance', 'Scheduled', 'Sports', 'Food', 'Photography']


countdict={}
for f in flairs:
    countdict[f]=0

countdict

data=[]
dataobj=[]
for i in sub.top('all',limit=None):
    dataobj.append(i)
print("---------data objects retrieved----------",len(dataobj))

for i in dataobj:
    if(i.link_flair_text in flairs):
        print(i,'-',i.link_flair_text)
        title=i.title
        body=i.selftext
        postflair=i.link_flair_text
        comments=[]
        subm=inst.submission(id=i.id)
        for com in subm.comments:
            if isinstance(com, MoreComments):
                continue
            comments.append(com.body)
        postext=title+' '+body+' '+' '.join(comments)
        data.append([postext,postflair])
        countdict[i.link_flair_text]+=1
print("--------Done Fetching Data---------")
df=pd.DataFrame(data)
df.to_csv("./precogdata.csv", sep=',',index=False)    
        
        