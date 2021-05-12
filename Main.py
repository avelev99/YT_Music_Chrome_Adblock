import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Utils import *


driver = webdriver.Chrome()
driver.get("https://music.youtube.com/")

wait = WebDriverWait(driver, 10)

def login():
    login_btn = driver.find_element_by_css_selector(".sign-in-link.ytmusic-nav-bar")
    login_btn.click()


login()





"""options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/chrome-win/chrome.exe"
chrome_driver_binary = "./Utils/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://music.youtube.com/")
#driver.find_element(By.NAME, "SIGN IN").send_keys("cheese" + Keys.RETURN)
#first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
#print(first_result.get_attribute("textContent"))

def Login():
    sign_in = driver.find_element_by_xpath("//button[text()='Sign in']")
    sign_in.click
    wait.until(EC.presence_of_element_located((By.ID, "identifierNext")))
    text_input(getUsername())

def text_input(text):
    action = ActionChains(driver)
    action.send_keys(text)
    action.perform()

def tabkey():
    driver.find_element(By.NAME, "q").send_keys(Keys.TAB)

Login()"""