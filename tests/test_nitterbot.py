import pytest

# test_how_long.py
from nitterbot import bot
from nitterbot import __version__
import datetime
from dateutil.tz import tzutc
from types import SimpleNamespace


# # https://github.com/halcy/Mastodon.py/blob/master/tests/conftest.py
# def _api(
#     access_token="__MASTODON_PY_TEST_ACCESS_TOKEN",
#     version="4.0.0",
#     version_check_mode="created",
# ):
#     import mastodon

#     return mastodon.Mastodon(
#         api_base_url="http://localhost:3000",
#         client_id="__MASTODON_PY_TEST_CLIENT_ID",
#         client_secret="__MASTODON_PY_TEST_CLIENT_SECRET",
#         access_token=access_token,
#         mastodon_version=version,
#         version_check_mode=version_check_mode,
#         user_agent="tests/v311",
#         debug_requests=True,
#     )


# @pytest.fixture
# def api():
#     return _api()


@pytest.fixture
def twitter_link():
    return "https://twitter.com/yuletide/status/1603949101154201603"


@pytest.fixture
def non_twitter_link():
    return "https://realpython.com/pytest-python-testing/"


@pytest.fixture
def status_with_twitter_link():
    return ""


@pytest.fixture
def status_linky():
    status_dict = {
        "id": 109572816854843079,
        "created_at": datetime.datetime(2022, 12, 25, 6, 8, 18, tzinfo=tzutc()),
        "in_reply_to_id": None,
        "in_reply_to_account_id": None,
        "sensitive": False,
        "spoiler_text": "",
        "visibility": "public",
        "language": "en",
        "uri": "https://mastodon.social/users/yuletide/statuses/109572816806684907",
        "url": "https://mastodon.social/@yuletide/109572816806684907",
        "replies_count": 0,
        "reblogs_count": 0,
        "favourites_count": 0,
        "edited_at": None,
        "favourited": False,
        "reblogged": False,
        "muted": False,
        "bookmarked": False,
        "content": '<p><span class="h-card"><a href="https://botsin.space/@nitterbot" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>nitterbot</span></a></span> help with link please <a href="https://twitter.com/yuletide/status/1603949101154201603" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="ellipsis">twitter.com/yuletide/status/16</span><span class="invisible">03949101154201603</span></a></p>',
        "filtered": [],
        "reblog": None,
        "account": {
            "id": 109391862882784405,
            "username": "yuletide",
            "acct": "yuletide@mastodon.social",
            "display_name": "alex yuletide",
            "locked": False,
            "bot": False,
            "discoverable": True,
            "group": False,
            "created_at": datetime.datetime(2022, 6, 21, 0, 0, tzinfo=tzutc()),
            "note": '<p>Spatial solutions arch &amp; web dev, social justice, civic tech, heavy metal.  Available for work! \u2028\u2029</p><p>Past: Mapbox Solutions Architect &amp; Tech Lead @ Community Team, <span class="h-card"><a href="https://mastodon.social/@recursecenter" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>recursecenter</span></a></span> fellow, founder of civic tech startup now part of @granicus, @codeforamerica fellow, @esri\u2029\u2028</p><p><a href="https://mastodon.social/tags/vegetarian" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>vegetarian</span></a> <a href="https://mastodon.social/tags/zen" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>zen</span></a> <a href="https://mastodon.social/tags/metal" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>metal</span></a> <a href="https://mastodon.social/tags/bassmusic" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>bassmusic</span></a> <a href="https://mastodon.social/tags/dj" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>dj</span></a> <a href="https://mastodon.social/tags/maps" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>maps</span></a> <a href="https://mastodon.social/tags/photography" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>photography</span></a> <a href="https://mastodon.social/tags/webdev" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>webdev</span></a> <a href="https://mastodon.social/tags/politics" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>politics</span></a></p>',
            "url": "https://mastodon.social/@yuletide",
            "avatar": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "avatar_static": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "header": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "header_static": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "followers_count": 148,
            "following_count": 78,
            "statuses_count": 153,
            "last_status_at": datetime.datetime(2022, 12, 25, 0, 0),
            "emojis": [],
            "fields": [
                {
                    "name": "Birdsite",
                    "value": '<a href="HTTPS://twitter.com/yuletide" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible"></span><span class="">HTTPS://twitter.com/yuletide</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
                {
                    "name": "LinkedSite",
                    "value": '<a href="https://linkedin.com/in/alexyule" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="">linkedin.com/in/alexyule</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
            ],
        },
        "media_attachments": [],
        "mentions": [
            {
                "id": 109543657746642932,
                "username": "nitterbot",
                "url": "https://botsin.space/@nitterbot",
                "acct": "nitterbot",
            }
        ],
        "tags": [],
        "emojis": [],
        "card": None,
        "poll": None,
    }
    # https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python
    # Library functions are expecting parsed objects not dicts so convert it over
    return SimpleNamespace(**status_dict)


@pytest.fixture
def status():
    status_dict = {
        "id": 109572761827885010,
        "created_at": datetime.datetime(2022, 12, 25, 5, 54, 18, tzinfo=tzutc()),
        "in_reply_to_id": None,
        "in_reply_to_account_id": None,
        "sensitive": False,
        "spoiler_text": "",
        "visibility": "public",
        "language": "en",
        "uri": "https://mastodon.social/users/yuletide/statuses/109572761775795910",
        "url": "https://mastodon.social/@yuletide/109572761775795910",
        "replies_count": 0,
        "reblogs_count": 0,
        "favourites_count": 0,
        "edited_at": None,
        "favourited": False,
        "reblogged": False,
        "muted": False,
        "bookmarked": False,
        "content": '<p><span class="h-card"><a href="https://botsin.space/@nitterbot" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>nitterbot</span></a></span> you ready for some twitter?</p>',
        "filtered": [],
        "reblog": None,
        "account": {
            "id": 109391862882784405,
            "username": "yuletide",
            "acct": "yuletide@mastodon.social",
            "display_name": "alex yuletide",
            "locked": False,
            "bot": False,
            "discoverable": True,
            "group": False,
            "created_at": datetime.datetime(2022, 6, 21, 0, 0, tzinfo=tzutc()),
            "note": '<p>Spatial solutions arch &amp; web dev, social justice, civic tech, heavy metal.  Available for work! \u2028\u2029</p><p>Past: Mapbox Solutions Architect &amp; Tech Lead @ Community Team, <span class="h-card"><a href="https://mastodon.social/@recursecenter" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>recursecenter</span></a></span> fellow, founder of civic tech startup now part of @granicus, @codeforamerica fellow, @esri\u2029\u2028</p><p><a href="https://mastodon.social/tags/vegetarian" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>vegetarian</span></a> <a href="https://mastodon.social/tags/zen" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>zen</span></a> <a href="https://mastodon.social/tags/metal" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>metal</span></a> <a href="https://mastodon.social/tags/bassmusic" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>bassmusic</span></a> <a href="https://mastodon.social/tags/dj" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>dj</span></a> <a href="https://mastodon.social/tags/maps" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>maps</span></a> <a href="https://mastodon.social/tags/photography" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>photography</span></a> <a href="https://mastodon.social/tags/webdev" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>webdev</span></a> <a href="https://mastodon.social/tags/politics" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>politics</span></a></p>',
            "url": "https://mastodon.social/@yuletide",
            "avatar": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "avatar_static": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "header": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "header_static": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "followers_count": 148,
            "following_count": 78,
            "statuses_count": 152,
            "last_status_at": datetime.datetime(2022, 12, 25, 0, 0),
            "emojis": [],
            "fields": [
                {
                    "name": "Birdsite",
                    "value": '<a href="HTTPS://twitter.com/yuletide" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible"></span><span class="">HTTPS://twitter.com/yuletide</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
                {
                    "name": "LinkedSite",
                    "value": '<a href="https://linkedin.com/in/alexyule" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="">linkedin.com/in/alexyule</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
            ],
        },
        "media_attachments": [],
        "mentions": [
            {
                "id": 109543657746642932,
                "username": "nitterbot",
                "url": "https://botsin.space/@nitterbot",
                "acct": "nitterbot",
            }
        ],
        "tags": [],
        "emojis": [],
        "card": None,
        "poll": None,
    }
    # https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python
    # Library functions are expecting parsed objects not dicts so convert it over
    return SimpleNamespace(**status_dict)


@pytest.fixture
def notification_linky_direct():
    return {
        "id": 6685320,
        "type": "mention",
        "created_at": datetime.datetime(2022, 12, 25, 6, 8, 19, 465000, tzinfo=tzutc()),
        "account": {
            "id": 109391862882784405,
            "username": "yuletide",
            "acct": "yuletide@mastodon.social",
            "display_name": "alex yuletide",
            "locked": False,
            "bot": False,
            "discoverable": True,
            "group": False,
            "created_at": datetime.datetime(2022, 6, 21, 0, 0, tzinfo=tzutc()),
            "note": '<p>Spatial solutions arch &amp; web dev, social justice, civic tech, heavy metal.  Available for work! \u2028\u2029</p><p>Past: Mapbox Solutions Architect &amp; Tech Lead @ Community Team, <span class="h-card"><a href="https://mastodon.social/@recursecenter" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>recursecenter</span></a></span> fellow, founder of civic tech startup now part of @granicus, @codeforamerica fellow, @esri\u2029\u2028</p><p><a href="https://mastodon.social/tags/vegetarian" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>vegetarian</span></a> <a href="https://mastodon.social/tags/zen" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>zen</span></a> <a href="https://mastodon.social/tags/metal" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>metal</span></a> <a href="https://mastodon.social/tags/bassmusic" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>bassmusic</span></a> <a href="https://mastodon.social/tags/dj" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>dj</span></a> <a href="https://mastodon.social/tags/maps" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>maps</span></a> <a href="https://mastodon.social/tags/photography" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>photography</span></a> <a href="https://mastodon.social/tags/webdev" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>webdev</span></a> <a href="https://mastodon.social/tags/politics" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>politics</span></a></p>',
            "url": "https://mastodon.social/@yuletide",
            "avatar": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "avatar_static": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "header": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "header_static": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "followers_count": 148,
            "following_count": 78,
            "statuses_count": 153,
            "last_status_at": datetime.datetime(2022, 12, 25, 0, 0),
            "emojis": [],
            "fields": [
                {
                    "name": "Birdsite",
                    "value": '<a href="HTTPS://twitter.com/yuletide" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible"></span><span class="">HTTPS://twitter.com/yuletide</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
                {
                    "name": "LinkedSite",
                    "value": '<a href="https://linkedin.com/in/alexyule" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="">linkedin.com/in/alexyule</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
            ],
        },
        "status": {
            "id": 109572816854843079,
            "created_at": datetime.datetime(2022, 12, 25, 6, 8, 18, tzinfo=tzutc()),
            "in_reply_to_id": None,
            "in_reply_to_account_id": None,
            "sensitive": False,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/yuletide/statuses/109572816806684907",
            "url": "https://mastodon.social/@yuletide/109572816806684907",
            "replies_count": 0,
            "reblogs_count": 0,
            "favourites_count": 0,
            "edited_at": None,
            "favourited": False,
            "reblogged": False,
            "muted": False,
            "bookmarked": False,
            "content": '<p><span class="h-card"><a href="https://botsin.space/@nitterbot" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>nitterbot</span></a></span> help with link please <a href="https://twitter.com/yuletide/status/1603949101154201603" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="ellipsis">twitter.com/yuletide/status/16</span><span class="invisible">03949101154201603</span></a></p>',
            "filtered": [],
            "reblog": None,
            "account": {
                "id": 109391862882784405,
                "username": "yuletide",
                "acct": "yuletide@mastodon.social",
                "display_name": "alex yuletide",
                "locked": False,
                "bot": False,
                "discoverable": True,
                "group": False,
                "created_at": datetime.datetime(2022, 6, 21, 0, 0, tzinfo=tzutc()),
                "note": '<p>Spatial solutions arch &amp; web dev, social justice, civic tech, heavy metal.  Available for work! \u2028\u2029</p><p>Past: Mapbox Solutions Architect &amp; Tech Lead @ Community Team, <span class="h-card"><a href="https://mastodon.social/@recursecenter" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>recursecenter</span></a></span> fellow, founder of civic tech startup now part of @granicus, @codeforamerica fellow, @esri\u2029\u2028</p><p><a href="https://mastodon.social/tags/vegetarian" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>vegetarian</span></a> <a href="https://mastodon.social/tags/zen" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>zen</span></a> <a href="https://mastodon.social/tags/metal" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>metal</span></a> <a href="https://mastodon.social/tags/bassmusic" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>bassmusic</span></a> <a href="https://mastodon.social/tags/dj" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>dj</span></a> <a href="https://mastodon.social/tags/maps" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>maps</span></a> <a href="https://mastodon.social/tags/photography" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>photography</span></a> <a href="https://mastodon.social/tags/webdev" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>webdev</span></a> <a href="https://mastodon.social/tags/politics" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>politics</span></a></p>',
                "url": "https://mastodon.social/@yuletide",
                "avatar": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
                "avatar_static": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
                "header": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
                "header_static": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
                "followers_count": 148,
                "following_count": 78,
                "statuses_count": 153,
                "last_status_at": datetime.datetime(2022, 12, 25, 0, 0),
                "emojis": [],
                "fields": [
                    {
                        "name": "Birdsite",
                        "value": '<a href="HTTPS://twitter.com/yuletide" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible"></span><span class="">HTTPS://twitter.com/yuletide</span><span class="invisible"></span></a>',
                        "verified_at": None,
                    },
                    {
                        "name": "LinkedSite",
                        "value": '<a href="https://linkedin.com/in/alexyule" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="">linkedin.com/in/alexyule</span><span class="invisible"></span></a>',
                        "verified_at": None,
                    },
                ],
            },
            "media_attachments": [],
            "mentions": [
                {
                    "id": 109543657746642932,
                    "username": "nitterbot",
                    "url": "https://botsin.space/@nitterbot",
                    "acct": "nitterbot",
                }
            ],
            "tags": [],
            "emojis": [],
            "card": None,
            "poll": None,
        },
    }


@pytest.fixture
def notification():
    return {
        "id": 6684837,
        "type": "mention",
        "created_at": datetime.datetime(
            2022, 12, 25, 5, 54, 19, 801000, tzinfo=tzutc()
        ),
        "account": {
            "id": 109391862882784405,
            "username": "yuletide",
            "acct": "yuletide@mastodon.social",
            "display_name": "alex yuletide",
            "locked": False,
            "bot": False,
            "discoverable": True,
            "group": False,
            "created_at": datetime.datetime(2022, 6, 21, 0, 0, tzinfo=tzutc()),
            "note": '<p>Spatial solutions arch &amp; web dev, social justice, civic tech, heavy metal.  Available for work! \u2028\u2029</p><p>Past: Mapbox Solutions Architect &amp; Tech Lead @ Community Team, <span class="h-card"><a href="https://mastodon.social/@recursecenter" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>recursecenter</span></a></span> fellow, founder of civic tech startup now part of @granicus, @codeforamerica fellow, @esri\u2029\u2028</p><p><a href="https://mastodon.social/tags/vegetarian" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>vegetarian</span></a> <a href="https://mastodon.social/tags/zen" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>zen</span></a> <a href="https://mastodon.social/tags/metal" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>metal</span></a> <a href="https://mastodon.social/tags/bassmusic" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>bassmusic</span></a> <a href="https://mastodon.social/tags/dj" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>dj</span></a> <a href="https://mastodon.social/tags/maps" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>maps</span></a> <a href="https://mastodon.social/tags/photography" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>photography</span></a> <a href="https://mastodon.social/tags/webdev" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>webdev</span></a> <a href="https://mastodon.social/tags/politics" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>politics</span></a></p>',
            "url": "https://mastodon.social/@yuletide",
            "avatar": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "avatar_static": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
            "header": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "header_static": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
            "followers_count": 148,
            "following_count": 78,
            "statuses_count": 152,
            "last_status_at": datetime.datetime(2022, 12, 25, 0, 0),
            "emojis": [],
            "fields": [
                {
                    "name": "Birdsite",
                    "value": '<a href="HTTPS://twitter.com/yuletide" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible"></span><span class="">HTTPS://twitter.com/yuletide</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
                {
                    "name": "LinkedSite",
                    "value": '<a href="https://linkedin.com/in/alexyule" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="">linkedin.com/in/alexyule</span><span class="invisible"></span></a>',
                    "verified_at": None,
                },
            ],
        },
        "status": {
            "id": 109572761827885010,
            "created_at": datetime.datetime(2022, 12, 25, 5, 54, 18, tzinfo=tzutc()),
            "in_reply_to_id": None,
            "in_reply_to_account_id": None,
            "sensitive": False,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/yuletide/statuses/109572761775795910",
            "url": "https://mastodon.social/@yuletide/109572761775795910",
            "replies_count": 0,
            "reblogs_count": 0,
            "favourites_count": 0,
            "edited_at": None,
            "favourited": False,
            "reblogged": False,
            "muted": False,
            "bookmarked": False,
            "content": '<p><span class="h-card"><a href="https://botsin.space/@nitterbot" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>nitterbot</span></a></span> you ready for some twitter?</p>',
            "filtered": [],
            "reblog": None,
            "account": {
                "id": 109391862882784405,
                "username": "yuletide",
                "acct": "yuletide@mastodon.social",
                "display_name": "alex yuletide",
                "locked": False,
                "bot": False,
                "discoverable": True,
                "group": False,
                "created_at": datetime.datetime(2022, 6, 21, 0, 0, tzinfo=tzutc()),
                "note": '<p>Spatial solutions arch &amp; web dev, social justice, civic tech, heavy metal.  Available for work! \u2028\u2029</p><p>Past: Mapbox Solutions Architect &amp; Tech Lead @ Community Team, <span class="h-card"><a href="https://mastodon.social/@recursecenter" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>recursecenter</span></a></span> fellow, founder of civic tech startup now part of @granicus, @codeforamerica fellow, @esri\u2029\u2028</p><p><a href="https://mastodon.social/tags/vegetarian" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>vegetarian</span></a> <a href="https://mastodon.social/tags/zen" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>zen</span></a> <a href="https://mastodon.social/tags/metal" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>metal</span></a> <a href="https://mastodon.social/tags/bassmusic" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>bassmusic</span></a> <a href="https://mastodon.social/tags/dj" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>dj</span></a> <a href="https://mastodon.social/tags/maps" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>maps</span></a> <a href="https://mastodon.social/tags/photography" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>photography</span></a> <a href="https://mastodon.social/tags/webdev" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>webdev</span></a> <a href="https://mastodon.social/tags/politics" class="mention hashtag" rel="nofollow noopener noreferrer" target="_blank">#<span>politics</span></a></p>',
                "url": "https://mastodon.social/@yuletide",
                "avatar": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
                "avatar_static": "https://files.botsin.space/cache/accounts/avatars/109/391/862/882/784/405/original/0efc492b3538e902.png",
                "header": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
                "header_static": "https://files.botsin.space/cache/accounts/headers/109/391/862/882/784/405/original/1f2a8c1cc92143b4.png",
                "followers_count": 148,
                "following_count": 78,
                "statuses_count": 152,
                "last_status_at": datetime.datetime(2022, 12, 25, 0, 0),
                "emojis": [],
                "fields": [
                    {
                        "name": "Birdsite",
                        "value": '<a href="HTTPS://twitter.com/yuletide" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible"></span><span class="">HTTPS://twitter.com/yuletide</span><span class="invisible"></span></a>',
                        "verified_at": None,
                    },
                    {
                        "name": "LinkedSite",
                        "value": '<a href="https://linkedin.com/in/alexyule" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="">linkedin.com/in/alexyule</span><span class="invisible"></span></a>',
                        "verified_at": None,
                    },
                ],
            },
            "media_attachments": [],
            "mentions": [
                {
                    "id": 109543657746642932,
                    "username": "nitterbot",
                    "url": "https://botsin.space/@nitterbot",
                    "acct": "nitterbot",
                }
            ],
            "tags": [],
            "emojis": [],
            "card": None,
            "poll": None,
        },
    }


def test_link_detection_with_twitter_link(twitter_link):
    assert bot.contains_twitter_link(twitter_link) is True


def test_link_detection_with_non_twitter_link(non_twitter_link):
    assert bot.contains_twitter_link(non_twitter_link) is False


def test_do_nothing_with_non_linky_status(status):
    assert bot.build_reply(status) is None


# circular logic?
def test_replace_links_in_linky_status(status_linky):
    reply = bot.build_reply(status_linky)
    assert bot.contains_twitter_link(reply) is False


def test_version():
    assert __version__ == "0.1.0"
