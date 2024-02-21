#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Reddit API URL for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "MyRedditBot/1.0"}
    
    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Extract number of subscribers from response
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        # Invalid subreddit or error occurred, return 0
        return 0
