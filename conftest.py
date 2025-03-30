import pytest
from modules.api.clients.github import Github
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page import SignInPage

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Taras'
        self.second_name = 'Yakushevych'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture()
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture()
def github_api():
    api = Github()

    yield api

@pytest.fixture()
def database():
    db = Database()

    yield db

@pytest.fixture()
def sign_in_page():
    sign_in = SignInPage()

    yield sign_in