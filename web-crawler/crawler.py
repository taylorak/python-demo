#!/usr/bin/env python
"A simple web crawler"

from collections import deque
import urllib.request
from urlparse import urljoin
from bs4 import BeautifulSoup


def crawler():
    "simple python web crawler"

    url_frontier = deque([
        'https://docs.python.org/2/library/collections.html'
        ])

    visited = set()

    while len(url_frontier):
        url = url_frontier.popleft()
        visited.add(url)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a'):
            print(link.get('href'))
            if link.startswith('http')

crawler()
