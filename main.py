from nitterbot import notifylistener
from nitterbot import bot


def main():
    listener = notifylistener.NotifyListener()
    mastodon = bot.init()
    mastodon.stream_user(listener)


if __name__ == "__main__":
    main()
