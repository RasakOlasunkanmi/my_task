# To run script: pip install pyshorteners

import pyshorteners


def shorten_url(long_url):

    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(long_url)


if __name__ == "__main__":
    long_url = input("Enter the URL you want to shorten: ")
    shortened = shorten_url(long_url)
    print("Shortened URL:", shortened)