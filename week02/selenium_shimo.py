from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    # 打开目标页面
    browser.get('https://shimo.im/welcome')
    # time.sleep(1)

    but = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    but.click()
    # 输入用户名、密码
    browser.find_element_by_xpath('//div/input[@name="mobileOrEmail"]').send_keys('12345@126.com')
    browser.find_element_by_xpath('//div/input[@name="password"]').send_keys('mimabunengxieichulai')
    # time.sleep(1)
    # 提交登录
    browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

    cookies = browser.get_cookies()
    print(cookies)
    # time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()