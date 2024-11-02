import pytest
from modules.api.clients.github import Github
import pprint

@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('yakushevych')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_can_not_be_found(github_api):
    r = github_api.search_repo('yakushevych_not_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_can_be_found_with_a_single_char(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0