#!/usr/bin/env python3
"""Retrieves and prints words from a URL.

Usage:
    python3 words.py <URL>
"""


import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetches a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(story_words):
    """Prints items one per line.

    Args:
        An iterable series of printable items.
    """
    for word in story_words:
        print(word)


def main(url):
    """Prints each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # The 0th arg is the module filename
