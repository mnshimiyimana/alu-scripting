#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
"""

import json
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        print(None)
