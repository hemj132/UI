from selenium.webdriver import Remote
from selenium import webdriver
import os
import sys

# 启动浏览器驱动
def browser():
    #driver = webdriver.Chrome()
    '''
    host = '127.0.0.1:4444' # 运行主机：端口号 （本机默认：127.0.0.1:4444）
    dc = {'browserName': 'chrome'} # 指定浏览器（'chrome','firefox',）
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    '''
    #返回当前运用文件目录
    #print(sys.path[0])
    path=os.path.join(sys.path[0],"model/chromedriver/chromedriver.exe")
    #path = sys.paht[0]+"/chromedriver/chromedriver.exe"
    driver= webdriver.Chrome(executable_path=path)
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
