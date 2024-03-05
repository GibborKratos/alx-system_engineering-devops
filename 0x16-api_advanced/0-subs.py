#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers={"User-Agent": "Mozilla/5.0"},
                            allow_redirects=False)
    
    if sub_info.status_code == 200: 
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
