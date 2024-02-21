#!/usr/bin/python3
"""function to query subscribers ona given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """ Return the total number of subscribers on a given subreddit. Reddit API URL for getting subreddit information"""
    url = f"https://www.reddit.com/r/{}/about.json". format(subreddit)
    headers = {
            "User-Agent":"linux:0x16.api.advance:v1.0.0 (by /u/bdov_}"
    
   response = reqests.get(url,headers=headers, allow_redirects=False)
   if response.status_code == 404:
   return 0
   results = response.json().get("data")
   return results.get("subscribers")
   
