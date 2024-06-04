#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
   This module retrieves hot posts from a given subreddit using pagination.
'''
import requests


BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''Retrieves a list of hot posts from a given subreddit.
       Args:
        subreddit: The name of the subreddit to search.
        hot_list:(list, optional)Accumulates titles of hot posts defaults to []
        after: (str, optional) A string representing the fullname of a post
                to use as a cursor for pagination. Defaults to None.

    Returns:
        list: A list containing titles of all hot posts,
              or None if an error occurs.
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
    sort = 'hot'
    limit = 30
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
