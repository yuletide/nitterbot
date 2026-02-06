from html.parser import HTMLParser
from urllib import request
import re

# https://stackoverflow.com/a/62180428/263926
# Converts HTML to text

# Pattern to match t.co shortened URLs
T_CO_URL_PATTERN = r"https?://t\.co/\S+"


class HTMLFilter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

    def link_parse(self, url: str):
        """
        Use a t.co url and expands it to the real url.
        """
        try:
            r = request.urlopen(url, timeout=10)
            return r.url
        except Exception as e:
            # If expansion fails, return the original URL
            # TODO: Use logging module instead of print
            print(f"Failed to expand t.co URL {url}: {e}")
            return url

    @classmethod
    def convert_html_to_text(cls, html: str) -> str:
        f = cls()
        f.feed(html)
        text = f.text
        # Match t.co URLs more precisely
        m = re.search(T_CO_URL_PATTERN, text)
        if m is not None:
            parsed_url = f.link_parse(m.group())
            text = re.sub(T_CO_URL_PATTERN, parsed_url, text, count=1)
        return text.strip()
