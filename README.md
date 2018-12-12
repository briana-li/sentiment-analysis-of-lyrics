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

Challenges: I had some difficulty figuring out how to extract the lyrics from the Genius API.
