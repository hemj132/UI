from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from model import myunit, function

from page_obj.login_page import LoginPage
from page_obj.mail_page import MailPage
from page_obj.home_page import homePage


class loginTest(myunit.MyTest):
    '''社区登录测试'''

    def test_login_user_pawd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action("","")
        sleep(2)
        self.assertEqual(po.login_error_hint(), '登录失败，请检查您的用户名或密码是否填写正确。')

    def test_login_pawd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action("testaaa","")
        sleep(2)
        self.assertEqual(po.login_error_hint(), '登录失败，请检查您的用户名或密码是否填写正确。')

    def test_login_user_pawd_error(self):
        '''用户名、密码为错误'''
        po = LoginPage(self.driver)
        po.open()
        character = random.choice('登录失败，请检查您的用户名或密码是否填写正确。')
        username = "test" + character
        po.login_action(username,"@#$%")
        sleep(2)
        self.assertEqual(po.login_error_hint(), '登录失败，请检查您的用户名或密码是否填写正确。')

    def test_login_success(self):
        '''用户名、密码正确，登录成功'''
        po = LoginPage(self.driver)
        po.open()
        user = "hemeijian"
        po.login_action(user,"123456")
        sleep(2)
        po2 = homePage(self.driver)
        self.assertEqual(po2.login_success_user(),'何美建')


if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(loginTest("test_login_success"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
