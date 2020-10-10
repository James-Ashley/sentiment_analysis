# This script accesses the News API to collect news articles on your keyword of choice.
import requests
import json
from config import n_key
import os
import pandas as pd
#run pip install nltk in your terminal with your PythonData environment activated if you have not already installed nltk
import nltk 
#nltk.download('vader_lexicon') <- you will need to run this the first time you run this code 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
SID = SentimentIntensityAnalyzer()


# n_key is your API key for NewsAPI
# keyword is the word you are interested in searching
# source_list is the list of US news sources available in NewsAPI
# initials is a string of your initials

def getNewsAPIData(n_key, keyword, domains, initials):
    base_url = ('http://newsapi.org/v2/everything?')
    params = {
        'language': 'en',
        'pageSize': 100,
        'sortBy': 'relevance',
        'apiKey': n_key,
        'q': keyword, 
        'domains': domains    
    }

    data_master = []
    for page_num in range(1, 4): 
        params['page'] = page_num
        response = requests.get(base_url, params)
        data = response.json()

        articles = data['articles']
        for index in range(0, len(articles)): 
            article_dict = {
                'Keyword': keyword,
                'Source': articles[index]['source']['name'],
                'Author': articles[index]['author'],
                'Title': articles[index]['title'],
                'URL': articles[index]['url'],
                'Text': articles[index]['content'],
                'Published': articles[index]['publishedAt']
            }
            data_master.append(article_dict)

    data_df = pd.DataFrame(data_master)
    data_df.to_csv(f'initial{keyword}NewsAPIdata{initials}.csv', index=False)

    data_df['compound score'] = data_df['title'].apply(lambda title: SID.polarity_scores(title)['compound'])
    data_df['negative score'] = data_df['title'].apply(lambda title: SID.polarity_scores(title)['neg'])
    data_df['positive score'] = data_df['title'].apply(lambda title: SID.polarity_scores(title)['pos'])
    data_df['neutral score'] = data_df['title'].apply(lambda title: SID.polarity_scores(title)['neu'])

    data_df.to_csv(f'sentiment{keyword}NewsAPIdata{initials}.csv', index=False)