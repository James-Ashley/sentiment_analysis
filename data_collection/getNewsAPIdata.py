import requests
import json
import os
import pandas as pd
#run pip install nltk in your terminal with your PythonData environment activated if you have not already installed nltk
import nltk 
# nltk.download('vader_lexicon') <- you will need to run this the first time you run this code 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
SID = SentimentIntensityAnalyzer()

# n_key is your API key for NewsAPI
# keywords is the list of words you are interested in searching
# source_list is the list of US news sources available in NewsAPI
# initials is a string of your initials
# this script will pull news articles based on your keyword searches and store the results in a csv file
# it will then use NLTK Vader to perform a sentiment analysis on the news headlines and store this in a new CSV file

def getNewsAPIData(n_key, keywords, domains, initials):
    # setting up the API url
    base_url = ('http://newsapi.org/v2/everything?')
    params = {
        'language': 'en',
        'pageSize': 100,
        'sortBy': 'relevance',
        'apiKey': n_key    
    }
    
    # empty list to store all API data
    data_master = []
    # create query for each keyword of interest
    for keyword in keywords:
        params['q'] = keyword
        # for each domain of interest, complete an API call that stores data in a list of dicts
        for domain in domains:
            params['domains'] = domain
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
                    'Published': articles[index]['publishedAt']}
                
                data_master.append(article_dict)

    # storing data in a DataFrame and to a CSV file
    data_df = pd.DataFrame(data_master)

    # performing sentiment analysis on the news headlines and storing in the dataframe
    data_df['compound score'] = data_df['Title'].apply(lambda title: SID.polarity_scores(title)['compound'])
    data_df['negative score'] = data_df['Title'].apply(lambda title: SID.polarity_scores(title)['neg'])
    data_df['positive score'] = data_df['Title'].apply(lambda title: SID.polarity_scores(title)['pos'])
    data_df['neutral score'] = data_df['Title'].apply(lambda title: SID.polarity_scores(title)['neu'])

    # saving to a new CSV file which includes API data and sentiment analysis
    data_df.to_csv(f'sentimentNewsAPIdata{initials}.csv', index=False)