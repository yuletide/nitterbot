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
            to_file="usercred.secret",
        )

    api = Mastodon(access_token="usercred.secret")
    return api


def build_reply(mention):
    # fetch reply
    # fetch status that reply was posted beneath
    # check status for twitter url
    # replace with nitter url
    # post reply
    # TODO: Allow for sepcifying a nitter instance
    reply_text = ""
    # if mention.text.find("twitter"):
    #     print("we found the disease, time to heal")
    #     reply_text = mention.text.replace("twitter.com", "unofficialbird.org")

    return reply_text
    print("creating reply")


# register()
mastodon = init()

# conversations = mastodon.conversations()

print("fetching mentions")
notifications = mastodon.notifications(types=["mention"])
# Returns a list of notification dicts.
for mention in notifications:
    # if notifications maintain read state we dont have to track previous replies at all
    # otherwise we need a datastore
    pp.pprint(mention)
    user = mention["account"]["username"]
    status = mention.status
    print(
        "found mention in reply to {user} id {id}".format(
            user=mention["account"]["username"], id=mention["account"]["id"]
        )
    )
    print(status.content)
    # reply = build_reply(mention)
    # mastodon.status_post(in_reply_to_id=mention.id, status=reply)
    # print("reply posted to post {id}" % id)
