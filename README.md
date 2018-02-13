# autotweet
Auto Tweet on Twitter based on certain keywords

# Requirements 
 - Docker
 - Twitter API keys

# Installation
 - Clone repository
 - cd autotweet
 - modify autotweet/codes/tweet.py and add the required twitter api keys
 - docker image build -t autotweet:1.0 .
 - docker run -d --name autoweet autotweet:1.0


