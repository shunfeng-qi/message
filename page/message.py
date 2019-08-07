import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Message(BaseAction):
    find_message = (By.ID,"com.android.mms:id/action_compose_new")
    @allure.step(title="点击进入填写电话和内容")
    def click_message(self,text):
        allure.attach("关键字",text,allure.attach_type.TEXT)
        allure.attach("关键字",text)
        self.click(self.find_message)
        #添加图片描述
        allure.attach("截图",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)
