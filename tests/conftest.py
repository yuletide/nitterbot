# flake8: noqa
import pytest
import datetime
from dateutil.tz import tzutc


class Objectify:
    def __init__(self, d):
        self.d = d

    def __repr__(self):
        return repr(self.d)

    def __get__(self, key):
        return self.d[key]

    def __getattr__(self, attr):
        result = self.d[attr]
        if isinstance(result, dict):
            return Objectify(result)
        return result


@pytest.fixture
def twitter_link():
    return "https://twitter.com/yuletide/status/1603949101154201603"

@pytest.fixture
def x_link():
   return "https://x.com/yuletide/status/1603949101154201603" 

@pytest.fixture
def non_twitter_link():
    return "https://realpython.com/pytest-python-testing/"


@pytest.fixture
def status_with_twitter_link():
    return ""


@pytest.fixture
def status_linky():
    _dict = {
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
    # Library functions are expecting parsed objects not dicts so convert it
    return Objectify(_dict)

# TODO refactor these tests
@pytest.fixture
def status_linky_x():
    _dict = {
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
        "content": '<p><span class="h-card"><a href="https://botsin.space/@nitterbot" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>nitterbot</span></a></span> help with link please <a href="https://x.com/yuletide/status/1603949101154201603" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="ellipsis">twitter.com/yuletide/status/16</span><span class="invisible">03949101154201603</span></a></p>',
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
    # Library functions are expecting parsed objects not dicts so convert it
    return Objectify(_dict)


@pytest.fixture
def status():
    _dict = {
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
    return Objectify(_dict)


@pytest.fixture
def notification_linky_direct():
    _dict = {
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
    return Objectify(_dict)


@pytest.fixture
def status_with_linky_parent():
    _dict = {
        "id": 109578127784819303,
        "created_at": datetime.datetime(2022, 12, 26, 4, 38, 57, tzinfo=tzutc()),
        "in_reply_to_id": 109578114775496862,
        "in_reply_to_account_id": 109391862882784405,
        "sensitive": False,
        "spoiler_text": "",
        "visibility": "private",
        "language": "en",
        "uri": "https://mastodon.social/users/yuletide/statuses/109578127752480580",
        "url": "https://mastodon.social/@yuletide/109578127752480580",
        "replies_count": 0,
        "reblogs_count": 0,
        "favourites_count": 0,
        "edited_at": None,
        "favourited": False,
        "reblogged": False,
        "muted": False,
        "bookmarked": False,
        "content": '<p><span class="h-card"><a href="https://botsin.space/@nitterbot" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>nitterbot</span></a></span> Please nitterify this post</p>',
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
            "statuses_count": 160,
            "last_status_at": datetime.datetime(2022, 12, 26, 0, 0),
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
    return Objectify(_dict)


@pytest.fixture
def linky_parent():
    _dict = {
        "id": 109578114775496862,
        "created_at": datetime.datetime(2022, 12, 26, 4, 35, 38, tzinfo=tzutc()),
        "in_reply_to_id": None,
        "in_reply_to_account_id": None,
        "sensitive": False,
        "spoiler_text": "",
        "visibility": "private",
        "language": "en",
        "uri": "https://mastodon.social/users/yuletide/statuses/109578114740971839",
        "url": "https://mastodon.social/@yuletide/109578114740971839",
        "replies_count": 0,
        "reblogs_count": 0,
        "favourites_count": 0,
        "edited_at": None,
        "favourited": False,
        "reblogged": False,
        "muted": False,
        "bookmarked": False,
        "content": '<p>This is a test post for bot testing with a link to twitter in it <a href="https://twitter.com/yuletide/status/1603949101154201603" rel="nofollow noopener noreferrer" target="_blank"><span class="invisible">https://</span><span class="ellipsis">twitter.com/yuletide/status/16</span><span class="invisible">03949101154201603</span></a></p>',
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
            "statuses_count": 160,
            "last_status_at": datetime.datetime(2022, 12, 26, 0, 0),
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
        "mentions": [],
        "tags": [],
        "emojis": [],
        "card": {
            "url": "https://twitter.com/yuletide/status/1603949101154201603",
            "title": "@yuletide@mastodon.social on Twitter",
            "description": "“I'm outta here. I'll leave this up for a while for posterity, and because I don't quite have the guts to nuke 15 years of content. But come say hi: @yuletide at mastodon dot social for active conversations\n\n#twittermigration #twitterpurge”",
            "type": "link",
            "author_name": "",
            "author_url": "",
            "provider_name": "Twitter",
            "provider_url": "",
            "html": "",
            "width": 0,
            "height": 0,
            "image": None,
            "embed_url": "",
            "blurhash": None,
        },
        "poll": None,
    }
    return Objectify(_dict)


@pytest.fixture
def notification_with_linky_parent(status_with_linky_parent):
    return Objectify(notification(status_with_linky_parent))


def notification(status):
    _dict = {
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
        "status": status,
    }
    return _dict
