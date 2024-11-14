from wsgiref.validate import assert_

import pytest
import pprint

@pytest.mark.api_get
def test_user_exist(github_api):
    user = github_api.get_user('Taras0310')
    assert user['login'] == 'Taras0310'



@pytest.mark.api_get
def test_user_not_exists(github_api):
    r = github_api.get_user('yakushevych')
    assert r['message'] == 'Not Found'

@pytest.mark.api_get
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api_get
def test_repo_can_not_be_found(github_api):
    r = github_api.search_repo('yakushevych_not_exist')
    assert r['total_count'] == 0

@pytest.mark.api_get
def test_repo_can_be_found_with_a_single_char(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api_update
def test_update_user_name(github_api):
    r = github_api.update_user_info(name = 'tarrik')
    assert r['name'] == 'tarrik'


@pytest.mark.api_update
def test_update_user_name_with_a_few_parameters(github_api):
    r = github_api.update_user_info(name = 'tarrik0310', twitter_username = 'Taras0310')
    assert r['name'] == 'tarrik0310'
    assert r['twitter_username'] == 'Taras0310'

@pytest.mark.api_get
def test_get_number_of_repos(github_api):
    r = github_api.get_repo('Taras0310', 'UPL')
    assert r['owner']['id'] == 75706669

@pytest.mark.api_update
def test_update_repos_name_with_a_valid_data(github_api):
    r = github_api.update_repo('Taras0310', 'UPL',  name = 'UPL321')
    body = r.json()
    assert body['name'] == 'UPL321'

@pytest.mark.api_update
def test_update_repos_name_with_a_valid_data_few_parameters(github_api):
    r = github_api.update_repo('Taras0310', 'UPL321',  name = 'UPL12345', description = 'UPLrepo')
    body = r.json()
    assert body['name'] == 'UPL12345'
    assert body['description'] == 'UPLrepo'
    #assert body['name'] == 'UPL32131'

@pytest.mark.api_update
def test_update_repos_name_with_the_invalid_data(github_api):
    r = github_api.update_repo('Taras0310', 'UPL', name = '')
    assert r.status_code == 422



@pytest.mark.api_delete
def test_delete_repo(github_api):
    r = github_api.delete_repo('Taras0310', 'Example')
    assert r.status_code == 404
    #assert r['private'] == 'False' - так написати не можемо, бо це тип респонс з бібліотеки requests, потрібно його перетворити в JSON  і тоді нам повернеться звичайний словник
    pprint.pprint(r.text) # поверне інформацію про респонс  "message":"Not '
 #'Found","documentation_url":"https://docs.github.com/rest/repos/repos#delete-a-repository","status":"404"}')

@pytest.mark.api_create
def test_craete_repo_with_a_valid_data(github_api):
    r = github_api.create_repo(name = 'Second API repo', description = 'My second repo created using API request')
    assert r.status_code == 201