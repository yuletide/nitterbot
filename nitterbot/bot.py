from dotenv import dotenv_values
from os.path import exists
from os import getenv

from mastodon import Mastodon

# from nitterbot.notifylistener import NotifyListener
from nitterbot.parser import HTMLFilter

# For debugging api responses
import pprint


pp = pprint.PrettyPrinter(indent=4)
config = dotenv_values(".env")
if "USER" in config:
    print("config loaded yay")
else:
    print("loading config from environment")
    config["USER"] = getenv("USER")
    print(config["USER"])
    config["PASSWORD"] = getenv("PASSWORD")
    config["ENV"] = getenv("ENV")
USER_CREDS = "usercred.secret"
CLIENT_CREDS = "clientcred.secret"

# TODO: Convert this to a class and make these all instance methods


def register():
    """Register the app with the server, only needs to be run once per instance
    to generate client secret"""
    print("creating app")
    Mastodon.create_app(
        "nitterbot",
        api_base_url="https://botsin.space/",
        to_file=CLIENT_CREDS,
    )


def init():
    """Initialize API by logging in and saving user token to file"""
    if exists(CLIENT_CREDS):
        print("client secret found")
    else:
        register()

    if exists(USER_CREDS):
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
            to_file=USER_CREDS,
        )

    api = Mastodon(access_token=USER_CREDS)
    return api


def build_reply(status):
    """
    # fetch reply
    # fetch status that reply was posted beneath
    # check status for twitter url
    # replace with nitter url
    # post reply
    # TODO: Allow for specifying a nitter instance
    """
    print(status)

    parsed = parse_status(status)

    reply_text = ""
    if contains_twitter_link(parsed):
        print("*birdsite detected, replacing*")
        reply_text = parsed.replace("twitter", "unofficialbird")
        print(reply_text)
        print("new status: {}".format(reply_text))
        return "Your nitterified status is ready: " + reply_text
        # mastodon.status_post(in_reply_to_id=status.id, status=reply_text)
    else:
        print("no birdsite found, checking parent")
        # pp.pprint(status)
        return


def process_mention(mention, api):
    user = mention.account
    status = mention.status
    print(
        "===== found mention in reply to {user} id {id} =====".format(
            user=user.username, id=user.id
        )
    )
    reply = build_reply(status)

    # api.status_post(in_reply_to_id=status.id, status=reply)
    if reply:
        print("Posting reply")
        api.status_reply(
            to_status=status, status=reply, untag=True, visibility="public"
        )
        print("reply posted")
    else:
        print("checking parent")
        # TODO move this into build_reply
        # TODO move api to class method
        if status.in_reply_to_id:
            parent = get_parent_status(status, api)
            parent_reply = build_reply(parent)
            if parent_reply:
                print("parent had twitter link!")
                print(parent_reply)
                print("Posting reply")
                api.status_reply(
                    to_status=status,
                    status=parent_reply,
                    untag=True,
                )
            else:
                print("no link found in parent, end of line")

    # print("reply posted to post {id}" % user.id)


# TODO make this regex, but it works...
def contains_twitter_link(text):
    return text.find("//twitter.com/") > 0


# def status_contains_twitter_link(status):
#     return contains_twitter_link(parse_status(status))


def parse_status(status):
    parsed = HTMLFilter.convert_html_to_text(status.content)
    print("filtered status {}".format(parsed))
    return parsed


def get_notifications(api):
    print("fetching mentions")
    notifications = api.notifications(types=["mention"])
    # Returns a list of notification dicts.
    for mention in notifications:
        # if notifications maintain read state we dont have to track previous replies
        # pp.pprint(mention)
        process_mention(mention, api)


def get_parent_status(_status, api):
    print("Fetching parent")
    parent = api.status(_status.in_reply_to_id)
    print(parent)
    return parent


if __name__ == "__main__":
    print("To run bot use python -m nitterbot")
