# Should we just move this function here or leave it in bot.py?
# bot.main()
# from nitterbot import bot

# bot.main()

from nitterbot.bot import init
from nitterbot.notifylistener import NotifyListener

print("Main")


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
