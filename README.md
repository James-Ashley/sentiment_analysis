# Sentiment Analysis of US English News Headlines on Immigration

Version 1.0.0

## Description
The purpose of this project to perform a sentiment analysis on newspaper headlines related to immigration.

## Background
Newspapers are notoriously biased, and research indicates that readers prefer news sources that affirm their beliefs and political leanings (Pew Research Center, 2014). This would suggest that news coverage, especially from more biased news sources, is not neutral. We were interested in exploring this by analyzing the sentiment of headlines covering a politically charged topic in the US: immigration.

## Data
News headlines from September 2020 through October 2020 were collected using the News API. We chose news domains that are also included in the Pew Research Center's political bias evaluation since we plan to evaluate the relationship between political bias and sentiment in the future (2014). We then evaluated the News on the Web Corpus for words related to immigration that occur frequently (Davies, 2020). We chose seven keywords for our API calls: immigration, immigrant(s), migrant(s), and refugee(s). We removed video headlines since our primary interest is in text sentiment and also removed news sources with fewer than 50 headlines for a more evenly distributed dataset. An overview of the number of headlines per source can be seen in the figure below.  

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/newssourcesindataset.png "Headlines per Source")

## Methods
Sentiment analysis was performed using NLTK Vader (Gilbert & Hutto, 2014). We used the same sentiment categories as (Chaithra, 2019): compound scores less than -0.2 were negative, compound scores above 0.2 were positive and all compound scores between this range were neutral. Using NLTK, we then converted the headlines to tokens with punctuation removed and performed a word frequency analysis.

## Results
As can be seen from the boxplots below, the median compound score was close to zero for all sources. 
![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/boxplotaveragecompoundscores.png "Boxplot Compound Scores" )

When looking at the percentages of sentiment categories per source, it is clear that both Breitbart and Al Jazeera English have a higher distribution of negative headlines than other sources. 

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/headlinesentimentspercent.png "Percent of Headlines by Sentiment Type")

As the figures below demonstrate, 'Trump' is the most frequently occurring word in both positive and negative headlines. 'Biden' is also frequent in both sets of headlines. The upcoming election seems to be heavily influencing news coverage even within a specific topic such as immigration. 

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/frequenttermspositive.png "Positive Headlines Keywords")

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/frequenttermsnegative.png "Negative Headlines Keywords")

Differences in topic become clearer when looking at word clouds (weighted by frequency). Positive headlines seem to focus more on the Supreme Court justice nomination while negative headlines seem to focus more on issues such as 'ICE' and the 'border'. 

#### Word Cloud of Positive Headlines

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/wordcloudpositive.png "Positive Headlines Word Cloud")

#### Word Cloud of Negative Headlines

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/wordcloudnegative.png "Negative Headlines Word Cloud")

## Limitations
Although NLTK Vader performs relatively well on a variety of datasets (Gilbert & Hutto, 2014), it was initially designed to evaluate the sentiment of social media and we did not verify its accuracy in our sentiment analysis. Future research should include created a training dataset of news headlines related to immigration to evaluate the accuracy of Vader and improve its performance.

In addition, as can be seen in the keyword analysis, the news cycle is heavily influenced by current events, and the News API only allowed us to access the last month of news stories. A dataset with a wider range of publication dates would allow us to more effectively look at the terms and topics that are frequent in positive vs. negative headlines. 

## Instructions
Before running this code, you should create an API Key for the News API. You should then run the code in the Jupyter Notebooks in the following folders in this order: 1) data_collection, 2) data_cleaning, and 3) data_analysis. You can customize your API calls to your domains and keywords of interest. 

## References 
Chaithra, V. D. (2019). Hybrid approach: naive bayes and sentiment VADER for analyzing sentiment of mobile unboxing video comments. *International Journal of Electrical and Computer Engineering (IJECE), 9*(5), 4452-4459.

Davies, Mark. (2016-) Corpus of News on the Web (NOW): 10 billion words from 20 countries, updated every day. Available online at https://www.english-corpora.org/now/.

Gilbert, C. H. E., & Hutto, E. (2014, June). Vader: A parsimonious rule-based model for sentiment analysis of social media text. In *Eighth International Conference on Weblogs and Social Media (ICWSM-14)*. Available at (20/04/16) http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf (Vol. 81, p. 82).

Martin, B. & Koufos, N. (2020). Sentiment analysis on Reddit news headlines with Python’s Natural Language Toolkit (NLTK). *Learn Data Science.* https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/.

Pew Research Center (2014). “Wave 1 American trends panel: Mar 19, 2014-Apr 29, 2014.” Washington, D.C. https://www.journalism.org/2014/10/21/political-polarization-media-habits/. 


## Contributors
James Ashley, Rebekah Callari-Kaczmarczyk, Rohan Patel, Ted Phillips, Morgan Spencer, Scot Wilson

## License and Copyright
&copy; James Ashley, Rebekah Callari-Kaczmarczyk, Rohan Patel, Ted Phillips, Morgan Spencer, Scot Wilson