import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emojis(github_api):
    r = github_api.get_emojis()
    assert (
        r["mango"]
        == "https://github.githubassets.com/images/icons/emoji/unicode/1f96d.png?v8"
    )


@pytest.mark.api
def test_user_followers_exists(github_api):
    r = github_api.get_user_followers("defunkt")
    ##print(f"Response is {r[0]}")
    assert len(r) > 0


@pytest.mark.api
def test_user_followers_error(github_api):
    r = github_api.get_user_followers("user_test")
    ##print(f"Response is {r}")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_users_following_target_user(github_api):
    r = github_api.get_users_following_target_user("mojombo", "defunkt")

    assert r.status_code == 204


@pytest.mark.api
def test_users_not_following_target_user(github_api):
    r = github_api.get_users_following_target_user("defunkt", "user_test")

    assert r.status_code == 404
