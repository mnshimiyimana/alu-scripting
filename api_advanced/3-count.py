#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of all hot articles.
"""

import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):

    """ First the counts dictionary"""
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}

    if after:
        params['after'] = after

    # Request of the result from reddit api.
    response = requests.get(url, headers=headers, params=params)

    # Read the result and retrieve the titles.
    if response.status_code == 200:

        data = response.json()
        after = data['data']['after']
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()

            # Look for the given words in your title.
            for word in word_list:
                word = word.lower()

                # use regex to avoid unnecessary punctuations around words.
                if re.search(rf'\b{word}\b', title):
                    if word in counts:
                        counts[word] += 1

                    else:
                        counts[word] = 1

        # recurse your function.
        if after:
            count_words(subreddit, word_list, after=after, counts=counts)

        # In descending order.
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for count in sorted_counts:
                print(f'{count[0]}: {count[1]}')

    # Print nothing if there is no subreddit given.
    else:
        return {}
