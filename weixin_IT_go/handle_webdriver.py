import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

for i in range(14):

    test_webdriver = webdriver.Chrome()
    test_webdriver.maximize_window()
    test_webdriver.get("https://www.wjx.cn/jq/46608790.aspx")

    ques1_sex = random.randint(1,2)
    ques1_sex = str(ques1_sex)
    above1 = above2 = test_webdriver.find_element_by_xpath("//li/a[@class='jqRadio' and @rel='q1_"+ques1_sex+"']")
    above1.click()

    ques1_sex = random.randint(1,5)
    ques1_sex = str(ques1_sex)
    above2 = test_webdriver.find_element_by_xpath("//li/a[@class='jqRadio' and @rel='q2_"+ques1_sex+"']")
    above2.click()



    above3 = test_webdriver.find_element_by_xpath("//li/a[@class='jqRadio' and @rel='q3_7']")
    above3.click()


    ques1_sex = random.randint(1,4)
    ques1_sex = str(ques1_sex)
    above4 = test_webdriver.find_element_by_xpath("//li/a[@class='jqRadio' and @rel='q4_"+ques1_sex+"']")
    above4.click()



    # 特点 ： 下拉框
    ques1_sex = random.randint(1,10)
    ques1_sex = str(ques1_sex)
    above5 = test_webdriver.find_element_by_xpath("//select[@id='q5']/option[@value='"+ques1_sex+"']")
    above5.click()

    for i in range(9):# 问题6-14
        m = i + 6
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()

    #  特点: 输入框
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q15']")
    above6.send_keys("无")

    # 问题16-23   8个   特点：radio
    for i in range(8):
        m = i + 16
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()

    #问题24 输入框
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q24']")
    above6.send_keys("无")

    #  25到32  8个 radio
    for i in range(8):
        m = i + 25
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()

    # 33  input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q33']")
    above6.send_keys("无")

    #34 7个  到 40
    for i in range(7):
        m = i + 34
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
    # 41 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q41']")
    above6.send_keys("无")

    # 42 7ge 48
    for i in range(7):
        m = i + 42
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
     # 49 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q49']")
    above6.send_keys("无")

    # 50 8 57
    for i in range(8):
        m = i + 50
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
    # 58 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q58']")
    above6.send_keys("无")

    # 59 7 65
    for i in range(7):
        m = i + 59
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
    # 66 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q66']")
    above6.send_keys("无")

    # 67 7 73
    for i in range(7):
        m = i + 67
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
    # 74 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q74']")
    above6.send_keys("无")


    # 75 7 81
    for i in range(7):
        m = i + 75
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
    # 82 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q82']")
    above6.send_keys("无")

    # 83 7 89
    for i in range(7):
        m = i + 83
        ques1_sex = random.randint(1, 4)
        ques1_sex = str(ques1_sex)
        s = "//li/a[@class='jqRadio' and @rel='q"+str(m)+"_"+ques1_sex+"']"
        print(s)
        above6 = test_webdriver.find_element_by_xpath(s)
        above6.click()
    # 90 input
    above6 = test_webdriver.find_element_by_xpath("//textarea[@id='q90']")
    above6.send_keys("无")

    # above4 = test_webdriver.find_element_by_xpath("//input[@value='提交']")
    # above4.click()


    time.sleep(120)
    test_webdriver.quit()