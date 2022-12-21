from nitterbot import Nitterbot
import bot

__version__ = "0.1.0"

if __name__ == "__main__":
    nitter = Nitterbot
    mastodon = bot.init()
    mastodon.stream_user(nitter)
