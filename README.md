# sentiment-analysis: TITLE HERE

Version 1.0.0

## Description
The purpose of this project to perform a sentiment analysis on newspaper headlines related to immigration.

## Background
Newspapers are notoriously biased and research suggests that readers prefer news sources that affirm their beliefs and political leanings (PEW RESEARCH HERE). This would suggest that news coverage, especially from more biased news sources, is not neutral. We were interested in verifying this by analyzing the sentiment of headlines covering a politically charged topic in the US: immigration. 

## Data
News headlines from September 2020 through October 2020 were collected using the News API. We chose news domains that are also included in the Pew Research Center's political bias evaluation since we plan to evaluate the relationship between political bias and sentiment in the future (CITATION HERE). We then evaluated the News on the Web Corpus for words related to immigration that occur frequently (CITATION HERE). We chose seven keywords for our API calls: immigration, immigrant(s), migrant(s), and refugee(s). We removed video headlines since our primary interest is in text sentiment and also removed news sources with fewer than 50 headlines for a more evenly distributed dataset. An overview of the number of headlines per source can be seen in the figure below.  

![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/newssourcesindataset.png "Headlines per Source")

## Methods
Sentiment analysis was performed using NLTK Vader (CITATION HERE). We used the same sentiment categories as SOURCE HERE: compound scores less than -0.2 were negative, compound scores above 0.2 were positive and all compound scores between this range were neutral. Using NLTK, we then converted the headlines to tokens with punctuation removed and performed a word frequency analysis using NLTK.

## Results
As can be seen from the boxplots below, the median compound score was close to zero for all sources. Sources
![alt text](https://github.com/James-Ashley/sentiment_analysis/blob/main/images/headlinesentimentspercent.png "Percent of Headlines by Sentiment Type")

## Limitations

## Instructions

## Contributors
Rebekah Callari-Kaczmarczyk

## License and Copyright
&copy; Rebekah Callari-Kaczmarczyk