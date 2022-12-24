from nitterbot.bot import init
from nitterbot.notifylistener import NotifyListener


def main():
    listener = NotifyListener()
    mastodon = init()
    # Mastodon.py currently does not support websocket based, multiplexed streams,
    # but might in the future.
    # https://mastodonpy.readthedocs.io/en/stable/10_streaming.html
    # mastodon.stream_user(listener, run_async=True)
    mastodon.status_post(status="Ready for posts")
    mastodon.stream_user(listener)


main()
