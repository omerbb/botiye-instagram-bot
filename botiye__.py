from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
a = 0

try:

    browser.get("https://www.instagram.com")
    sleep(7)

    username = browser.find_element_by_name("username")
    password = browser.find_element_by_name("password")


    username.send_keys("botiye__")
    sleep(1)
    password.send_keys("xxtrax55")
    password.send_keys(Keys.RETURN)
    sleep(7)
    del username, password

    simdi_deil = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    simdi_deil.click()
    sleep(7)
    del simdi_deil


    try:
        simdi_deil2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        simdi_deil2.click()
        del simdi_deil2
    except:
        pass

    sleep(25)
    browser.quit()
except:
    browser.quit()
