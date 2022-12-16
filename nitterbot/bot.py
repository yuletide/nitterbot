from mastodon import Mastodon


def reply(mention):
    # fetch reply
    # fetch status that reply was posted beneath
    # check status for twitter url
    # replace with nitter url
    # post reply
    # TODO: Allow for sepcifying a nitter instance
    print("creating reply")


# Register your app! This only needs to be done once (per server, or when
# distributing rather than hosting an application, most likely per device and server).
# Uncomment the code and substitute in your information:
# """
# print("creating app")
# Mastodon.create_app(
#     "nitterbot",
#     api_base_url="https://botsin.space/",
#     to_file="clientcred.secret",
# )
# """

# Then, log in. This can be done every time your application starts (e.g. when writing a
# simple bot), or you can use the persisted information:
mastodon = Mastodon(
    client_id="clientcred.secret",
)

mastodon.log_in(code="usercred.secret")

# mastodon = Mastodon(access_token="token.secret", api_base_url="https://bostin.space")

# mastodon.status_post("hello world!")

convos = mastodon.conversations()

print(convos)

print("fetching mentions")
notifications = mastodon.notifications(types=["mention"])
# Returns a list of notification dicts.
for mention in notifications:
    print(mention)
    reply(mention)

print(notifications)
