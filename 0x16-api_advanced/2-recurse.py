#!/usr/bin/python3
"""
Use recursion to return a list of all hot post titles for a given subreddit
"""

import requests


def get_url(subreddit):
    """returns the url for a given subreddit"""
    return 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)


headers = {
    'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/aaorrico23)'
}


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    if after is None:
        return hot_list

    url = get_url(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        js = r.json()
    except ValueError:
        return None

    try:
        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))
    except Exception:
        return None

    return recurse(subreddit, hot_list, after)
