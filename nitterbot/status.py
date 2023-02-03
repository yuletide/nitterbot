class Status:
    def __init__(self, status_text: str):
        self.text = status_text
        self.nitterurl = nitterurl

    def check_twitter_link() -> bool:
        return True

    def compose_reply():
        return ""


class MastodonAPI:
    def __init__(self, user: str, password: str):
        self.mastodon = do_the_login(user, password)

    def parse_notification(self, notification):
        return Status(notification.status_text)

    def create_listener(self):
        self.mastodon.listener(self.callback)

    def callback(notification):
        s = parse_notification(notification)
        if s.check_twitter_link():
            return s.compose_reply
