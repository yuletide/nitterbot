from mastodon.streaming import StreamListener


class Nitterbot(StreamListener):
    def on_notification(self, notification):
        print("notification received {}".format(notification))
        return super().on_notification(notification)
