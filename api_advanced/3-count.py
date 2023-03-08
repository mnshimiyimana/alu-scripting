#!/usr/bin/python3
"""Recursively queries the Reddit API, parses the title of all hot articles, 
"""
import requests



def count_words(subreddit, word_list, after=None, counts={}):
    """
        Recursively queries the Reddit API and passes the results to a helper function.
    """
    headers = {'User-Agent': 'mybot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    
    if after is None:
        counts = {}

    if after:
        url += f'&after={after}'
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code != 200:
        return None
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title']
        words = title.lower().split()
        for word in word_list:
            word = word.lower()
            if word in words:
                counts[word] = counts.get(word, 0) + words.count(word)
    after = data['data']['after']
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print(f'{count[0]}: {count[1]}')
        return
    count_words(subreddit, word_list, after=after, counts=counts)
