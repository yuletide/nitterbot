import pytest

# test_how_long.py
from nitterbot import bot
from nitterbot import __version__


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
