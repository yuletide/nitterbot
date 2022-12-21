from nitterbot import notifylistener
from nitterbot import bot

listener = notifylistener.NotifyListener()
mastodon = bot.init()
mastodon.stream_user(listener)
