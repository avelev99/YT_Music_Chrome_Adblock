import gc
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Utils import *

collected = gc.collect()

driver = webdriver.Chrome()
driver.get("https://music.youtube.com/")

wait = WebDriverWait(driver, 10)

def login():
    login_btn = driver.find_element_by_css_selector(".sign-in-link.ytmusic-nav-bar")
    login_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'identifierId')))

def ins_text(text):
    actions = ActionChains(driver)
    actions.send_keys(text)
    actions.perform()

"""def next():
    ActionChains(driver).send_keys(Keys.TAB * 2).perform()"""

login()

collected = gc.collect()

print("Garbage collection thresholds:",
                    gc.get_threshold())
print("Garbage collector: collected",
            "%d objects." % collected)