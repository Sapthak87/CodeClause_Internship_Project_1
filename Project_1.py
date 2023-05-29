
#install the module pyshorteners
#pip install pyshorteners

import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()

    shortened_url = shortener.tinyurl.short(url)
    return shortened_url

long_url = input("Enter an URL: ")
short_url = shorten_url(long_url)
print(f"Short URL: {short_url}")