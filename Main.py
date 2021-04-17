from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

#This example requires Selenium WebDriver 3.13 or newer

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/chrome-win/chrome.exe"
chrome_driver_binary = "./Utils/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://music.youtube.com/")
driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
print(first_result.get_attribute("textContent"))