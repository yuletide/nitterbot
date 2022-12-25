from nitterbot.notifylistener import NotifyListener
from nitterbot import bot

# This file was created to help deploy to railway
# TODO: Move this logic back to the module


def main():
    listener = NotifyListener()
    mastodon = bot.init()
    # Mastodon.py currently does not support websocket based, multiplexed streams,
    # but might in the future.
    # https://mastodonpy.readthedocs.io/en/stable/10_streaming.html
    # mastodon.stream_user(listener, run_async=True)
    mastodon.status_post(status="Ready for posts", visibility="unlisted")
    mastodon.stream_user(listener)


if __name__ == "__main__":
    main()
