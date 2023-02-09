# test_how_long.py
from unittest.mock import Mock

from nitterbot import bot
from nitterbot import __version__

# import pytest

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


# def test_respond_to_linky_parent(linky_parent):
#

# circular logic?
def test_replace_links_in_linky_status(status_linky):
    reply = bot.build_reply(status_linky)
    assert bot.contains_twitter_link(reply) is False


def test_linky_status_too_long():
    # placeholder
    pass


def test_respond_to_notification_with_linky_parent_status(
    notification_with_linky_parent, linky_parent
):
    api = Mock()
    api.status.return_value = linky_parent
    print(notification_with_linky_parent)
    assert notification_with_linky_parent is not None

    bot.process_mention(notification_with_linky_parent, api)

    api.status.assert_called_once_with(
        notification_with_linky_parent.status.in_reply_to_id
    )
    api.status_reply.assert_called_once_with(
        to_status=notification_with_linky_parent.status,
        status=bot.build_reply(linky_parent),
        untag=True,
        visibility="public",
    )


# @pytest.mark.vcr()
# def test_get_status_parent(status_with_linky_parent, linky_parent):
#     api = bot.init()
#     parent = bot.get_parent_status(status_with_linky_parent, api)
#     assert parent == linky_parent


# @pytest.mark.vcr()
# def test_login():
#     bot.init()


def test_version():
    assert __version__ == "0.3.0"
