from django.shortcuts import render
from django import forms
import requests
import praw as pr
from praw.models import MoreComments
import pickle as pk
import pandas as pd



inst=pr.Reddit(client_id='3OfPLZHksCkemA',
                     client_secret='MvF8ObKoHJ8PNAFDh00WdSx8Y9E',
                     password='precogreddit',
                     user_agent='testscript',
                     username='DikshantSagar')

sub=inst.subreddit('india')
numdict={
     0:'Politics',
    1: 'Non-Political',
    2: 'AskIndia',
    3: '[R]eddiquette',
    4: 'Science/Technology',
    5: 'Policy/Economy',
    6: 'Business/Finance',
    7: 'Scheduled',
    8: 'Sports',
    9: 'Food',
    10: 'Photography'
}


def home(request):
    return render(request,'index.html')

def output(request):
    flair='DEBUG'
    if request.method=='POST':
        url=request.POST['link']
        submission=inst.submission(url=url)
        text=submission.selftext
        title=submission.title
        comments=[]
        for com in submission.comments:
            if isinstance(com, MoreComments):
                continue
            comments.append(com.body)
        postext=title+' '+text+' '+' '.join(comments)
        test=pd.DataFrame([postext])
        test.replace('\d+', 'NUM', regex=True)
        file1=open('tfidf.obj','rb')
        tfidf=pk.load(file1)
        file2=open('model.obj','rb')
        model=pk.load(file2)
        test=tfidf.transform(test.iloc[:,0])
        pred=numdict[model.predict(test)[0]]
    return render(request,'index.html',{'flair':pred})
