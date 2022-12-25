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


# @pytest.fixture
# def api():
#     return _api()


@pytest.fixture
def status(api):

    _status = api.status_post("Test status!")
    yield _status
    api.status_delete(_status["id"])


@pytest.fixture
def twitter_link():
    return "https://twitter.com/yuletide/status/1603949101154201603"


@pytest.fixture
def non_twitter_link():
    return "https://realpython.com/pytest-python-testing/"


@pytest.fixture
def status_with_twitter_link():
    return ""


def test_link_detection_with_twitter_link(twitter_link):
    assert bot.contains_twitter_link(twitter_link) is True


def test_link_detection_with_non_twitter_link(non_twitter_link):
    assert bot.contains_twitter_link(non_twitter_link) is False


def test_replace_links_in_status(status_with_twitter_link):
    assert bot.contains_twitter_link(bot.build_reply(status_with_twitter_link)) is False


def test_version():
    assert __version__ == "0.1.0"
