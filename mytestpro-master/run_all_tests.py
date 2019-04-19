import unittest
from HTMLTestRunner3 import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib,os


# 发送测试报告，需要配置你的邮箱账号。
def send_mail(file_new):
    mail_from='717474445@qq.com'
    mail_to='18501629830@163.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=u"自动化测试报告"
    smtp=smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('717474445@qq.com','eymjmxqvqimabehb')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print('email has send out !')


# 查找最新生成的测试报告
def get_new_file(files):
    lists = os.listdir(files)
    lists.sort(key=lambda fn: os.path.getmtime(files+"\\"+fn))
    file_ = os.path.join(files,lists[-1])
    print(file_)
    return file_


if __name__ == '__main__':
    test_app = "./mail_app" #定义测试应用
    now_time =  time.strftime("%Y_%m_%d_%H_%M_%S")
    reportfile=test_app+"/report/"+now_time+"result.html"
    fp = open(reportfile,'wb')
    runner = HTMLTestRunner(fp,
                           title="xxx测试报告",
                           description="运行环境：windows 10, chrome")
    discover = unittest.defaultTestLoader.discover(test_app+"/test_case", pattern='*_case.py')
    runner.run(discover)
    fp.close()
    # suite = unittest.TestSuite()  # 创建测试套件
    # all_cases = unittest.defaultTestLoader.discover(test_app+"/test_case", pattern='*_case.py')
    # # 找到某个目录下所有的以test开头的Python文件里面的测试用例
    # for case in all_cases:
    #     suite.addTests(case)  # 把所有的测试用例添加进来
    #
    # # runner = HTMLTestRunner(stream=fp, title='all_tests', description='运行环境：windows 10, chrome')
    # # runner.run(suite)
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
   # send_mail(get_new_file('./mail_app/report/'))
#    #  send_mail('D:\\codespace\\UI\\mytestpro-master\\mail_app\\report\\2019_04_19_11_21_07result.html')