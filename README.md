# lyrics-sentiment-analysis
In this project, I worked on analyzing the sentiment of lyrics from 10 different artists' 10 most popular
songs. 

Essentially, I did this in three steps: data collection of song lyrics using the Genius API and BeautifulSoup for scraping the lyrics from the HTML, analyzing the lexical diversity of the lyrics using word clouds and matplotlib and generating sentiment analysis. 

I tried to use artists from various genres. They were the following:
* Ariana Grande (pop)
* Bring Me The Horizon (rock)
* Eminem (hip-hop)
* Frank Ocean (R&B)
* John Mayer (pop)
* Keith Urban (country)
* Linkin Park (rock)
* My Chemical Romance (punk-rock)
* Pharrell Williams (pop)
* Tauren Wells (Christian pop)

In order to run the program you must have the following packages installed: nltk, pandas, matplotlib, bs4, urllib and wordcloud

To run the program, you must get a client ID, client secret key, and a client access token from https://genius.com/api-clients

These codes are used in "credentials.ini" and "songs.py" 

## Data Collection ##
To collect the data, run 
`"python3 songs.py"` 

to collect the lyrics of the top 10 songs from the artists listed in the "config.py" file. This class uses the search function from "search.py" which is a [python wrapper](https://github.com/jasonqng/genius-lyrics-search) for getting the lyrics from the Genius API. It essentially can accept the name of an artist, and then return urls of the lyrics for songs by that artist. I then used BeautifulSoup to find the "lyrics" html tag from Genius.com. I also did some basic data cleaning to get rid of words like "Chorus" and "Verse 1". You can run this using `"python3 clean_data.py"`

## Analyze Text Using Wordclouds ##
We can now perform some tests on the frequency of the words using `"python3 text_analysis.py"` in which we plot the number of words and the lexical richness of the artists for the ten songs. According to our results, Eminem has the most number of words. To find the lexical richness, we divide the number of words by the number of unique words used by each artist and filter out stopwords. Frank Ocean and Eminem seem to have the highet lexical richness. 

We can also call `"python3 wordclouds.py"` to generate word clouds for each artist. 

## Sentiment Analysis ##
I analyzed the sentiment of the lyrics using NLTK's Vader Sentiment analyzer. This analyzer is sensitive to both polarity (positive/negative) and intensity (strength) of emotion. You can read more about it [here](https://github.com/cjhutto/vaderSentiment). 

Challenges: I had some difficulty figuring out how to extract the lyrics from the Genius API.
