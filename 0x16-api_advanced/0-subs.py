#!/usr/bin/python3
'''Module to interact with the Reddit API.
'''
import requests

BASE_URL = 'https://www.reddit.com'
'''Base URL for Reddit's API.
'''


def number_of_subscribers(subreddit):
    '''Fetches the number of subscribers for a specified subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: Number of subscribers if the subreddit is valid, otherwise 0.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }

    try:
        response = requests.get(
            '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
            headers=api_headers,
            allow_redirects=False
        )

        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
