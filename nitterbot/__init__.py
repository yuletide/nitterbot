import notifylistener
import bot

__version__ = "0.1.0"

if __name__ == "__main__":
    listener = notifylistener.NotifyListener()
    mastodon = bot.init()
    mastodon.stream_user(listener)
