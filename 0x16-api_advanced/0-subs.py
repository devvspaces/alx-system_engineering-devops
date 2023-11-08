#!/usr/bin/python3
"""
Get the number of subscribers for a given subreddit
"""

import requests


def get_url(subreddit):
    """returns the url for a given subreddit"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    return url


headers = {
    'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'
}


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(get_url(subreddit), headers=headers).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
