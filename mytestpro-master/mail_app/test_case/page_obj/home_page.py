from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base


class homePage(Base):
    url  = "/"
    login_success_user_loc = (By.ID,"myname")

    def login_success_user(self):
        return str(self.find_element(*self.login_success_user_loc).text).replace(' ','')