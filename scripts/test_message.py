from base.base_driver import init_driver
from page.page import Page
import time
import pytest
class TestMessage:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.allure.serverity(pytest.allure.serverity_level.BLOCKER)
    @pytest.mark.parametrize(("phone","contact"),[("18888888888","你好"),("17777777777","hello")])
    def test_message(self,phone,contact):
        self.page.message.click_message()
        self.page.message_page.input_message_page(phone)
        self.page.message_page.input_message_input(contact)
        self.page.message_page.click_btn()