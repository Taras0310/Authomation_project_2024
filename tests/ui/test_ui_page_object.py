from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object(sign_in_page):


    sign_in_page.go_to()

    sign_in_page.try_to_login('taras0310', 'test12345')

    sign_in_page.close()