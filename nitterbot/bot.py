from mastodon import Mastodon

from dotenv import dotenv_values
from os.path import exists
import pprint


pp = pprint.PrettyPrinter(indent=4)
config = dotenv_values(".env")
USER_CREDS = "usercred.secret"


def register():
    # This only needs to be done once per server
    print("creating app")
    Mastodon.create_app(
        "nitterbot",
        api_base_url="https://botsin.space/",
        to_file="clientcred.secret",
    )


def init():

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


def build_reply(content):
    # fetch reply
    # fetch status that reply was posted beneath
    # check status for twitter url
    # replace with nitter url
    # post reply
    # TODO: Allow for sepcifying a nitter instance
    reply_text = ""
    if content.find("twitter") > 0:
        print("*birdsite detected, replacing*")
        reply_text = content.replace("twitter", "unofficialbird")
        print(reply_text)
        print("new status: {}".format(reply_text))
        # mastodon.status_post(in_reply_to_id=status.id, status=reply_text)
    else:
        print("no birdsite found, skipping")
        return

    return reply_text


def get_notifications(api):
    print("fetching mentions")
    notifications = api.notifications(types=["mention"])
    # Returns a list of notification dicts.
    for mention in notifications:
        # if notifications maintain read state we dont have to track previous replies
        # pp.pprint(mention)
        user = mention["account"]
        status = mention.status
        print(
            "===== found mention in reply to {user} id {id} =====".format(
                user=user.username, id=user.id
            )
        )
        print(status.content)
        print(status.content.find("twitter"))
        if status.content.find("twitter") > 0:
            print("*birdsite detected, replacing*")
            reply_text = status.content.replace("twitter", "unofficialbird")
            print(reply_text)
            print("new status: {}".format(reply_text))
            # api.status_post(in_reply_to_id=status.id, status=reply_text)
        else:
            print("no birdsite found, skipping")

        # mastodon.status_post(in_reply_to_id=mention.id, status=reply)
        # print("reply posted to post {id}" % id)


if __name__ == "__main__":
    # procedural script approach
    api = init()
    get_notifications(api)
