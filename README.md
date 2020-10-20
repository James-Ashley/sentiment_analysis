# Sentiment Analysis of US English News Headlines on Immigration

Version 1.0.0

## Description
The purpose of this project to perform a sentiment analysis on newspaper headlines related to immigration.

## Background
Newspapers are notoriously biased and research suggests that readers prefer news sources that affirm their beliefs and political leanings (PEW RESEARCH HERE). This would suggest that news coverage, especially from more biased news sources, is not neutral. We were interested in verifying this by analyzing the sentiment of headlines covering a politically charged topic in the US: immigration. 

## Data
News headlines from September 2020 through October 2020 were collected using the News API. We chose news domains that are also included in the Pew Research Center's political bias evaluation since we plan to evaluate the relationship between political bias and sentiment in the future (CITATION HERE). We then evaluated the News on the Web Corpus for words related to immigration that occur frequently (CITATION HERE). We chose seven keywords for our API calls: immigration, immigrant(s), migrant(s), and refugee(s). We removed video headlines since our primary interest is in text sentiment and also removed news sources with fewer than 50 headlines for a more evenly distributed dataset. An overview of the number of headlines per source can be seen in the figure below.  

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/newssourcesindataset.png "Headlines per Source")

## Methods
Sentiment analysis was performed using NLTK Vader (CITATION HERE). We used the same sentiment categories as SOURCE HERE: compound scores less than -0.2 were negative, compound scores above 0.2 were positive and all compound scores between this range were neutral. Using NLTK, we then converted the headlines to tokens with punctuation removed and performed a word frequency analysis.

## Results
As can be seen from the boxplots below, the median compound score was close to zero for all sources. 
![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/boxplotaveragecompoundscores.png =100x20 "Boxplot Compound Scores" )

When looking at the percentages of sentiment categories per source, it is clear that both Breitbart and Al Jazeera English have a higher distribution of negative headlines than other sources. 

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/headlinesentimentspercent.png "Percent of Headlines by Sentiment Type")

As the figures below demonstrate, 'Trump' is the most frequently occurring word in both positive and negative headlines. 'Biden' is also frequent in both sets of headlines. The upcoming election seems to be heavily influencing news coverage even within a specific topic such as immigration. 

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/frequenttermspositive.png "Positive Headlines Keywords")

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/frequenttermsnegative.png "Negative Headlines Keywords")

Differences in topic become clearer when looking at word clouds (weighted by frequency). Positive headlines seem to focus more on the Supreme Court justice nomination while negative headlines seem to focus more on issues such as 'ICE' and the 'border'. 

### Word Cloud of Positive Headlines

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/wordcloudpositive.png "Positive Headlines Word Cloud")

### Word Cloud of Negative Headlines

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/wordcloudnegative.png "Negative Headlines Word Cloud")

## Limitations

## Instructions

## Contributors
Rebekah Callari-Kaczmarczyk

## License and Copyright
&copy; Rebekah Callari-Kaczmarczyk