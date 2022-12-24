from html.parser import HTMLParser

# https://stackoverflow.com/a/62180428/263926
# Converts HTML to text


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data

    @classmethod
    def convert_html_to_text(cls, html: str) -> str:
        f = cls()
        f.feed(html)
        return f.text.strip()
