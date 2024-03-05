#!/usr/bin/python3
"""
function that should print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }
        response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
	if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")

    # Print the titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]
