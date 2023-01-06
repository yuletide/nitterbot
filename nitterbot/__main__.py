from nitterbot.bot import init, config
from nitterbot.notifylistener import NotifyListener
from mastodon.errors import MastodonNetworkError
from mastodon.errors import MastodonInternalServerError
from time import sleep


def main():
    listener = NotifyListener()
    mastodon = init()

    # Don't post a status if we are testing locally
    if not config["ENV"] == "DEV":
        mastodon.status_post(
            status="New deploy or recovering from crash. Ready for posts!",
            visibility="private",
        )
    try:
        # Mastodon.py currently does not support websocket based, multiplexed streams,
        # but might in the future.
        # https://mastodonpy.readthedocs.io/en/stable/10_streaming.html
        # mastodon.stream_user(listener, run_async=True)
        mastodon.stream_user(listener)
    except MastodonNetworkError as err:
        print("Network error, reinitializing", err)
        main()  # TODO: refactor here
    except MastodonInternalServerError as err:
        print("Internal server error, what is going on?", err)
        # Pause to avoid some strange errors
        sleep(10)
        main()


main()
