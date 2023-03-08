#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            title = post['data']['title']
            hot_list.append(title)

        # set after to the last post of the previous result.
        after = data['data']['after']

        # call the function with the updated after i.e recursion
        if after:
            recurse(subreddit, hot_list, after)

    else:
        return None

    return hot_list
