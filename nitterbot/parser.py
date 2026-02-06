from html.parser import HTMLParser
from urllib import request
from urllib.error import URLError
import re

# https://stackoverflow.com/a/62180428/263926
# Converts HTML to text


class HTMLFilter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

    def link_parse(self, url: str):
        """
        use a t.co url and expands it to the real url.
        """
        try:
            r = request.urlopen(url, timeout=10)
            return r.url
        except (URLError, Exception) as e:
            # If expansion fails, return the original URL
            print(f"Failed to expand t.co URL {url}: {e}")
            return url

    @classmethod
    def convert_html_to_text(cls, html: str) -> str:
        f = cls()
        f.feed(html)
        text = f.text
        # Match t.co URLs more precisely
        m = re.search(r"https?://t\.co/\S+", text)
        if m is not None:
            parsed_url = f.link_parse(m.group())
            text = re.sub(r"https?://t\.co/\S+", parsed_url, text, count=1)
        return text.strip()
