from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas
import time
def get_score():
    username = "405290319"
    password = "ling5851"
    url = "http://stu.fju.edu.tw/stusql/SingleSignOn/StuScore/stu_login.htm"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile = profile)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    input_level = driver.find_element_by_xpath('/html/body/span/table/tbody/tr[5]/td/form/div[2]/center/p/input')
    input_level.click()
    input_level.send_keys(username)
    time.sleep(0.5)
    input_level = driver.find_element_by_xpath('/html/body/span/table/tbody/tr[5]/td/form/div[3]/center/p/input')
    input_level.click()
    input_level.send_keys(password)
    time.sleep(0.5)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/span/table/tbody/tr[5]/td/form/div[4]/center/p/input[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/span/p/table/tbody/tr/td/form/div[3]/center/p/input").click()
    all_num = 0
    all_score = 0
    for i in range(2,32):
        try:
            get = driver.find_element_by_xpath('/html/body/div[2]/center/table/tbody/tr[{}]/td[3]'.format(i))
            num =  eval(driver.find_element_by_xpath("/html/body/div[2]/center/table/tbody/tr[{}]/td[4]".format(i)).text)
            all_num += num
            score = eval(driver.find_element_by_xpath("/html/body/div[2]/center/table/tbody/tr[{}]/td[6]".format(i)).text)
            all_score += score*num
        except Exception as e:
            break
        print(get.text ,num,score)
    print(all_score/all_num)
    driver.close()
    driver.quit()
get_score()
