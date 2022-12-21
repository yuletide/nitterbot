# Nitterbot
Basic bot that converts twitter links of any kind to nitter.net or similar

Requirements:
* Poetry
* .env file with login info 


## TODO
 *  write some tests
 * rewrite using the stream API to avoid persistence since we don't care about the past here, only the future!
    > Callbacks for the streaming API. Create a subclass, override the on_xxx methods for the kinds of events you’re interested in, then pass an instance of your subclass to Mastodon.user_stream(), Mastodon.public_stream(), or Mastodon.hashtag_stream().

References

https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/

https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1#Dependency-Management

https://gist.github.com/aparrish/661fca5ce7b4882a8c6823db12d42d26

https://www.programcreek.com/python/?project_name=zigg%2Ffediplay# 