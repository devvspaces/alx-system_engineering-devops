#!/usr/bin/python3
"""
Count the number of times a keyword appears in the titles of hot posts
"""

import requests


def get_url(subreddit, after=None):
    '''returns the url for a given subreddit'''
    return 'http://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)


def count_words(subreddit, word_list, found_list=[], after=None):
    """
    Return the number of times a keyword appears in the titles of hot posts

    :param subreddit: subreddit to search
    :type subreddit: str
    :param word_list: list of words to search for
    :type word_list: list
    :param found_list: list of words found, defaults to []
    :type found_list: list, optional
    :param after: after, defaults to None
    :type after: str, optional
    """
    user_agent = {'User-agent': 'Mozilla/5.0'}
    posts = requests.get(get_url(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
