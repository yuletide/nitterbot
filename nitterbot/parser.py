from html.parser import HTMLParser
from urllib import request
import re

# https://stackoverflow.com/a/62180428/263926
# Converts HTML to text


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data

    def link_parse(self, url: str):
        """
        use a t.co url and expands it to the real url.
        """
        r = request.urlopen(url)
        return r.url

    @classmethod
    def convert_html_to_text(cls, html: str) -> str:
        f = cls()
        f.feed(html)
        text = f.text
        m = re.search(r"\bhttps?://t.co(.*)\b", text)
        if m is not None:
            parsed_url = f.link_parse(m.group())
            text = re.sub(r"\bhttps?://t.co(.*)\b", parsed_url, text)
        return text.strip()
