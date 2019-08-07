from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessagePage(BaseAction):
    find_message_page = By.XPATH,"//*[@text='接收者']"
    find_message_input = By.XPATH,"//*[@text='键入信息']"
    find_btn = By.ID,"com.android.mms:id/send_button_sms"

    def input_message_page(self,text):
        self.input(self.find_message_page,text)
    def input_message_input(self,message):
        self.input(self.find_message_input,message)
    def click_btn(self):
        self.click(self.find_btn)