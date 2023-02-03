# import pprint

from mastodon import Mastodon
from os.path import exists
from os import getenv


def register(client_creds):
    """Register the app with the server, only needs to be run once per instance
    to generate client secret"""
    print("creating app")
    Mastodon.create_app(
        "nitterbot",
        api_base_url="https://botsin.space/",
        to_file=client_creds,
    )


API = None


def get_api(config):
    global API
    if API is not None:
        return API
    # pp = pprint.PrettyPrinter(indent=4)
    if "USER" in config:
        print("config loaded yay")
    else:
        print("loading config from environment")
        config["USER"] = getenv("USER")
        # print(config["USER"])
        config["PASSWORD"] = getenv("PASSWORD")
        config["ENV"] = getenv("ENV")
    user_creds = "usercred.secret"
    client_creds = "clientcred.secret"

    # Initialize API by logging in and saving user token to file
    if exists(client_creds):
        print("client secret found")
    else:
        register(client_creds)

    if exists(user_creds):
        print("user token already found")
    else:
        # Then, log in. This can be done every time your application starts (e.g. when
        # writing a simple bot), or you can use the persisted information:
        mastodon = Mastodon(
            client_id="clientcred.secret",
        )
        print("logging in")
        mastodon.log_in(
            username=config["USER"],
            password=config["PASSWORD"],
            to_file=user_creds,
        )

    API = Mastodon(access_token=user_creds)
    return API
