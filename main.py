from nitterbot import notifylistener
from nitterbot import bot


def main():
    listener = notifylistener.NotifyListener()
    mastodon = bot.init()
    # Mastodon.py currently does not support websocket based, multiplexed streams,
    # but might in the future.
    # https://mastodonpy.readthedocs.io/en/stable/10_streaming.html
    mastodon.stream_user(listener, run_async=True)


if __name__ == "__main__":
    main()
