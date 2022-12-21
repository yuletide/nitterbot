from mastodon.streaming import StreamListener
from nitterbot.bot import process_mention, init


class NotifyListener(StreamListener):
    def __init__(self) -> None:
        print("**listening**")
        self.api = init()
        super().__init__()

    def on_notification(self, notification):
        print("notification received {}".format(notification))
        if notification.type == "mention":
            process_mention(notification, self.api)
        return super().on_notification(notification)
