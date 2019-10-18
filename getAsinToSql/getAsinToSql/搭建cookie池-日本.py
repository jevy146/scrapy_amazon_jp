# @File  : IT搭建cookie池-删除重新获取.py
# @Author: Jie Wei
#@time: 2019/7/26 17:47

# @File  : 01-selenium获取cookie，.py
# @Author: Jie Wei
#@time: 2019/7/26 9:23



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random
import numpy as np
import json
from selenium.webdriver.common.action_chains import ActionChains  #控制鼠标进行点击的
from selenium.common.exceptions import  TimeoutException
chrome_options = Options()
ua = UserAgent()
url="https://www.amazon.co.jp"
#NoImage = {"profile.managed_default_content_settings.images": 2}  # 控制 没有图片
#chrome_options.add_experimental_option("prefs", NoImage)
chrome_options.add_argument(f'user-agent={ua.random}')  # 增加浏览器头部
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)
# browser.maximize_window()  # 在这里登陆的中国大陆的邮编

#browser.maximize_window()
# browser.set_window_size(1400, 900)

start_time = time.time()
def click_address():
    global wait
    try:
        browser.get(url)
        button_change_address = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#nav-global-location-slot > span > a')))  # 点击选择定位的，
        button_change_address.click()
        time.sleep(random.randint(1, 3))
        input_0 = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#GLUXZipUpdateInput_0'))
        )
        input_0.send_keys("197")  # 输入邮编。。
        time.sleep(0.8)
        input_1 = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#GLUXZipUpdateInput_1'))
        )
        input_1.send_keys("0804")  # 输入邮编。。
        # print('点击设置。。')
        time.sleep(random.randint(1, 3))
        button_set = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#GLUXZipUpdate > span > input')))

        time.sleep(1)
        button_set.click()
        try:
            time.sleep(random.randint(2, 4))
            button_done =wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#GLUXConfirmClose')))  # 跟美国的不一样。
            button_done.click()  # fertig 按钮。
            print("按钮点击完成。。")
        except:
            ActionChains(browser).move_by_offset(200, 400).click().perform()  # 鼠标左键点击， 200为x坐标， 100为y坐标
            print("鼠标点击")
        time.sleep(random.randint(1, 3))
        total = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#glow-ingress-line2')))
        end_time = time.time()
        print("出现邮编结果", total.text)
        print("总用时间，，", end_time - start_time)
    except TimeoutException :
        click_address()


count=0


while True:
    click_address()  # 点击动作。。
    browser.refresh() #刷新一下。。

    count+=1
    print(f"正在进行今天的第{count}次抓取cookie")
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#glow-ingress-line2')))
    print("出现邮编结果", total.text)
    time.sleep(30)
    get_cookie=browser.get_cookies()  # 点击生成的cookie
    print(get_cookie)
        #保存cookie
    file = open("cookies_17.txt", "w")
    json.dump(get_cookie, file)
    file.close()
    print("保存新的cookie完成")
    time.sleep(np.random.randint(600, 900))  # 休息等10-12分钟
    browser.delete_all_cookies()  # 先删除原来的cookie，再从新获取。。
    time.sleep(1)
    browser.refresh()  #第一次没有加这个。。第一项没有，不刷新也可以，，省的加载界面，比较慢，，

    # time.sleep(30) #休息等8-12分钟



# import redis
# client=redis.StrictRedis()
# client.lpush("cookies",json.dumps(get_cookie))  #
# print(client)
