#!/usr/bin/python3
"""
Get the titles of the first 10 hot posts for a given subreddit
"""

import requests


def get_url(subreddit):
    """returns the url for a given subreddit"""
    return 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)


headers = {
    'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'
}


def top_ten(subreddit):
    """Display the titles of the first 10 hot
    posts listed for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    r = requests.get(
        get_url(subreddit),
        headers=headers,
        params={'limit': 10}).json()
    posts = r.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
