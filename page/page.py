from page.message import Message
from page.message_page import MessagePage


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def message(self):
        return Message(self.driver)
    @property
    def message_page(self):
        return MessagePage(self.driver)